from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.models import CustomUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    avatar = forms.ImageField(required=False)  # Optional upload

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'avatar']
