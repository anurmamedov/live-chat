from django.urls import path
from .views import Check_Username

app_name = 'main'

urlpatterns = [
    path('/check-username', Check_Username, name='check'),
]