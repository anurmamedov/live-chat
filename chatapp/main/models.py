from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, default='avatars/default-avatar.jpg')

    def __str__(self):
        return self.username


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'senders')
    content = models.TextField(max_length=250)
    date = models.DateTimeField(default=now)


    def __str__(self):
       return f"{self.sender.username} : {self.content}"
    