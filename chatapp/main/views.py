from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pathlib import Path
from .models import MyUser

def main_view(request):
    return render(request, 'main.html', {})


def serve_css(request):
    css_file_path = Path(__file__).resolve().parent / 'templates/output.css'
    with open(css_file_path, 'r') as f:
        return HttpResponse(f.read(), content_type='text/css')
    

def check_username(request):
    get_username = request.POST.get('input-username')
    if MyUser.objects.filter(username=get_username).exists():
        return JsonResponse({
            'user_exists': True 
        })
    return JsonResponse({
        'user_exists': False
    })
    
