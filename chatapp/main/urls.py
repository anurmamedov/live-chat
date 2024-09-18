from django.urls import path
from .views import check_username

app_name = 'main'

urlpatterns = [
    path('username', check_username, name='check_username'),
]