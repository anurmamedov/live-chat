from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pathlib import Path
from .models import MyUser

def main_view(request):
    print(MyUser.objects.all())
    return render(request, 'main.html', {})


def serve_css(request):
    css_file_path = Path(__file__).resolve().parent / 'templates/output.css'
    with open(css_file_path, 'r') as f:
        return HttpResponse(f.read(), content_type='text/css')
    

def check_username(request):
    get_username = request.POST.get('input-username')
    if MyUser.objects.filter(username=get_username).exists():
        return JsonResponse({
            'user_already_exists': True 
        })
    else:
        MyUser.objects.create(username=get_username)
        return JsonResponse({
            'user_created': True,
            'user_already_exists': False
        })
