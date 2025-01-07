from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pathlib import Path
from django.contrib.auth.models import User


def main_view(request):
    users = User.objects.all()
    return render(request, 'main.html', {'users': users})


def serve_css(request):
    css_file_path = Path(__file__).resolve().parent / 'templates/output.css'
    with open(css_file_path, 'r') as f:
        return HttpResponse(f.read(), content_type='text/css')
    


    


