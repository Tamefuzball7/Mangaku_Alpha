from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(default="", blank=True, max_length=14000)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    fondo = models.ImageField(default='default.jpg', upload_to='profile_fondos')
    profesion = models.CharField( max_length=100 )
    celular = models.CharField( max_length=20)
    pais = models.CharField( max_length=100)
    genero = models.CharField( max_length=10)
    
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
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
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
	
	




	

	


















