from django.urls import path
from .views import send_message

app_name = 'main'

urlpatterns = [
    path('send', send_message, name='send-message'),
]
