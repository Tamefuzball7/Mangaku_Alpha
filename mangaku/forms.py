from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    profesion = forms.CharField(max_length=100)
    celular = forms.CharField(max_length=20)
    pais = forms.CharField(max_length=100)
    genero = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['first_name',"last_name", 'username', 'email', 'password1', 'password2','profesion', 'celular', 'pais', 'genero']


class PostForm(forms.ModelForm):
	content = forms.CharField()
	class Meta:
		model = Post
		fields = ['content']

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'username' ,'last_name',"email"]

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image', 'bio', "fondo",'profesion', 'celular', 'pais', 'genero']





















