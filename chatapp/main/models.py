from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class MyUser(models.Model):
    username = models.TextField(max_length=20)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')

