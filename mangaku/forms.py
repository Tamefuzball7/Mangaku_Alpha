from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile




class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Nombre'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Apellidos'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Usuario'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input100', 'placeholder': 'Correo Electrónico'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Confirmar Contraseña'}))
    phone_number = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Número de teléfono'}))
    CHOICES = [('male', 'Hombre'), ('female', 'Mujer')]
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'input100', 'placeholder': 'Selecciona el género'}))

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






















