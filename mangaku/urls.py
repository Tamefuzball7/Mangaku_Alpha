from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from .views import about







urlpatterns = [
	path('', views.home, name='home'),
	path('register/', views.register, name='register'),
	path('login/', LoginView.as_view(template_name='mangaku/login.html'), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('delete/<int:post_id>/', views.delete, name='delete'),
	path('profile/<str:username>/', views.profile, name='profile'),
	path('editar/', views.editar, name='editar'),
	path('follow/<str:username>/', views.follow, name='follow'),
	path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
	path('favicon.ico', RedirectView.as_view(url='mangaku/static/img/logo.png'), name='favicon'),
    path('about/<str:username>/', views.about, name='about'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('dislike/<int:post_id>/', views.dislike_post, name='dislike_post'),
    path('posts/<int:post_id>/', views.detalle_post, name='detalle_post'),
    path('fotos/<str:username>/', views.fotos, name='fotos'),
    path('chat/<str:username>/', views.chat, name='chat'),
    

    
    
    
    
    




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
