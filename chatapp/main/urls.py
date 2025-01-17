from django.urls import path
from .views import send_message, display_messages

app_name = 'main'

urlpatterns = [
    path('send', send_message, name='send-message'),
    path('display', display_messages, name='display-messages'),
]
