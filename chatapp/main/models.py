from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(models.Model):
    username = models.TextField(max_length=20)
