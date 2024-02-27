from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    vorname = forms.CharField(max_length=40)
    nachname = forms.CharField(max_length=50)

    class Meta:
        model=User
        fields = ['vorname', 'nachname', 'username', 'password1', 'password2']