from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    profession = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=20)
    country = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['first_name',"last_name", 'username', 'email', 'password1', 'password2','profession', 'phone_number', 'country', 'gender']


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
		fields = ['image', 'bio', "fondo",'profession', 'phone_number', 'country', 'gender']





















