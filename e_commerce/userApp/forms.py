from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
# from .models import Post

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields } # Remueve las Ayudas


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'UserName or email',
            }
        )
    )

    password = forms.CharField(
        label='Contraseña', 
        widget=forms.PasswordInput(
            attrs = {
                'placeholder': 'password'
            }
        )
    )