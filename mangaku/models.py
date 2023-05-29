from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verificado = models.BooleanField(default=False)
    bio = models.CharField(default="", blank=True, max_length=200)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    fondo = models.ImageField(default='default.jpg', upload_to='profile_fondos' )
    profession = models.CharField( max_length=100, blank=True )
    phone_number = models.CharField( max_length=20, blank=True)
    country = models.CharField( max_length=100, blank=True)
    gender = models.CharField( max_length=10, blank=True)
    birthday = models.DateField(null=True, blank=True)
    
    
    def __str__(self):
        return f'Perfil de {self.user.username}:'

    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.user)\
                                    .values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)

    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self.user)\
                                    .values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)

		
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



class Post(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(blank=True, null=True ,default="", upload_to='image_posts')  # Campo de imagen
    content = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    comments = models.ManyToManyField(User, through='Comment', related_name='commented_posts')
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_posts', blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.content
    
    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    
class Relationship(models.Model):
	from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_comments', blank=True)

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()
    
   


	
	




	

	


















