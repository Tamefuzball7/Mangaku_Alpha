from django.shortcuts import render, redirect , get_object_or_404
from .models import Profile, Post, Relationship, Comment
from .forms import UserRegisterForm, PostForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from random import sample
from django.http import HttpResponse ,JsonResponse


@login_required
def home(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    context = {'posts': posts, 'form': form}
    return render(request, 'mangaku/newsfeed.html', context)

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
        post.dislikes.remove(request.user)  # Eliminar dislike si existe
    return redirect('home')

@login_required
def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.dislikes.all():
        post.dislikes.remove(request.user)
    else:
        post.dislikes.add(request.user)
        post.likes.remove(request.user)  # Eliminar like si existe
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
        # Si el comentario no pertenece al usuario autenticado, mostrar un mensaje de error o redirigir a otra página
        return HttpResponse('No tienes permiso para editar este comentario.')

    if request.method == 'POST':
        content = request.POST.get('content')
        comment.content = content
        comment.save()
        # Redirigir a la página de comentarios o hacer cualquier otra acción después de guardar los cambios

    context = {'user': User, 'post': Post, 'comment': comment}
    return render(request, 'mangaku/editar_comentario.html', context)

def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post_id=post_id)
    comment.delete()
    return redirect('home')

@login_required
def search(request):
    query = request.GET.get('q')
    profiles = Profile.objects.filter(user__username__icontains=query)
    return render(request, 'mangaku/search.html', {'profiles': profiles})






