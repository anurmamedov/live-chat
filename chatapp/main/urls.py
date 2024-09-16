from django.urls import path
from .views import my_view

app_name = 'main'

urlpatterns = [
    path('username', my_view, name='my_view'),
]