from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.models import CustomUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    avatar = forms.ImageField(required=False)  # Optional upload

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'avatar']


    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar and avatar.size > 5 * 1024 * 1024:  # Limit file size to 5MB
            raise forms.ValidationError("Avatar file size should not exceed 5MB.")
        return avatar