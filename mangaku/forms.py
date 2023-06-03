from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    gender = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['first_name',"last_name", 'username', 'email', 'password1', 'password2', 'phone_number', 'gender']


class PostForm(forms.ModelForm):
    content = forms.CharField(required=False)
    imagen = forms.ImageField(required=False)
    

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        imagen = cleaned_data.get('imagen')

        if not content and not imagen:
            raise forms.ValidationError('Debes subir al menos una imagen o ingresar un contenido.')

        return cleaned_data

    class Meta:
        model = Post
        fields = ['content', 'imagen' ]

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'username' ,'last_name',"email"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'fondo', 'profession', 'phone_number', 'country', 'gender']
        widgets = {
            'bio': forms.Textarea(),
        }
        labels = {
            'bio': 'Biografía',
        }
        required = {
            'image': False,
            'bio': False,
            'fondo': False,
            'profession': False,
            'phone_number': False,
            'country': False,
            'gender': False,
        }






















