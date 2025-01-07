from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now



# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'senders')
    content = models.TextField(max_length=250)
    date = models.DateTimeField(default=now)


    def __str__(self):
       return self.sender.username + " : " + self.content
