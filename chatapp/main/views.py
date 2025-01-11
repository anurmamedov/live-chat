from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pathlib import Path
from django.contrib.auth.models import User
from .models import Message
import json
from django.http import JsonResponse, HttpResponseBadRequest


def main_view(request):
    users = User.objects.all()
    return render(request, 'main.html', {'users': users})


def send_message(request):
    print(request)
    body = json.loads(request.body)
    print(body)
    print(body['username'])
    print(body['content'])
    username = body['username']
    content = body['content']
    # # print(username) 
    # # print(content) 
    user = User.objects.get(username=username)
    # print(user)
    new_message = Message.objects.create(sender=user, content=content)
    new_message.save()
    return render(request, 'main.html')


def serve_css(request):
    css_file_path = Path(__file__).resolve().parent / 'templates/output.css'
    with open(css_file_path, 'r') as f:
        return HttpResponse(f.read(), content_type='text/css')
    
