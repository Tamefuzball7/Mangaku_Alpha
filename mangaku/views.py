from django.shortcuts import render, redirect , get_object_or_404
from .models import Profile, Post, Relationship, Comment
from .forms import UserRegisterForm, PostForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from random import sample
from django.http import HttpResponse ,JsonResponse
from django.db.models import Q, Case, When , F
from django.contrib.postgres.search import TrigramSimilarity 
from django.db.models.signals import pre_delete
from django.dispatch import receiver




@login_required
def home(request):
    user = request.user
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    context = {'posts': posts, 'form': form,'user': user }
    return render(request, 'mangaku/newsfeed.html', context    )

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = UserRegisterForm()

	context = {'form' : form}
	return render(request, 'mangaku/register.html', context)

def delete(request, post_id):
	post = Post.objects.get(id=post_id)
	post.delete()
	return redirect('home')

def profile(request, username):
    user = User.objects.get(username=username)
    posts = user.posts.all()
    context = {'user': user, 'posts': posts}
    return render(request, 'mangaku/profile.html', context)

@login_required
def editar(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            birthday = request.POST.get('birthday')
            request.user.profile.birthday = birthday
            request.user.profile.save()

            return redirect('editar')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'mangaku/editar.html', context)


@login_required
def follow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()
	return redirect('home')

@login_required
def unfollow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user.id
	rel = Relationship.objects.get(from_user=current_user.id, to_user=to_user_id)
	rel.delete()
	return redirect('home')

@login_required
def about(request, username):
	user = User.objects.get(username=username)
	posts = user.posts.all()
	context = {'user':user, 'posts':posts}
	return render(request, 'mangaku/about.html', context)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        post.dislikes.remove(request.user) 
    return redirect('home')

@login_required
def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.dislikes.all():
        post.dislikes.remove(request.user)
    else:
        post.dislikes.add(request.user)
        post.likes.remove(request.user) 
    return redirect('home')

@login_required
def fotos (request, username):
	user = User.objects.get(username=username)
	posts = user.posts.all()
	context = {'user':user, 'posts':posts}
	return render(request, 'mangaku/fotos.html', context)

@login_required
def chat (request, username):
	user = User.objects.get(username=username)
	posts = user.posts.all()
	context = {'user':user, 'posts':posts}
	return render(request, 'mangaku/chat.html', context)

@login_required
def comentarios(request, username, post_id):
    user = get_object_or_404(User, username=username)
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        comment = Comment(user=request.user, post=post, content=content)
        comment.save()

    comments = Comment.objects.filter(post=post)
    comments_with_profiles = comments.select_related('user__profile')

    context = {'user': user, 'post': post, 'comments': comments_with_profiles}
    return render(request, 'mangaku/comentarios.html', context)

@login_required
def editar_comentario(request, username, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user != request.user:
        
        return HttpResponse('No tienes permiso para editar este comentario.')

    if request.method == 'POST':
        content = request.POST.get('content')
        comment.content = content
        comment.save()
        

    context = {'user': User, 'post': Post, 'comment': comment}
    return render(request, 'mangaku/editar_comentario.html', context)

def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post_id=post_id)
    comment.delete()
    return redirect('home')


@login_required
def search(request):
    query = request.GET.get('q')
    profiles = []

    if query:
        profiles = Profile.objects.annotate(
            similarity=TrigramSimilarity('user__username', query) +
                       TrigramSimilarity('user__first_name', query) +
                       TrigramSimilarity('user__last_name', query)
        ).filter(
            Q(user__username__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).order_by(
            Case(When(similarity__gt=0.1, then=-1*F('similarity')), default=-1*F('similarity'))
        )

    return render(request, 'mangaku/search.html', {'profiles': profiles})


@receiver(pre_delete, sender=Post)
def eliminar_archivo(sender, instance, **kwargs):
    # Eliminar el archivo asociado al post
    instance.imagen.delete(save=False)


@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
        comment.dislikes.remove(request.user)  
        return redirect('home')

@login_required
def dislike_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.user in comment.dislikes.all():
        comment.dislikes.remove(request.user)
    else:
        comment.dislikes.add(request.user)
        comment.likes.remove(request.user)  
        return redirect('home')
    
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('home')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'mangaku/change_password.html', {'form': form})






