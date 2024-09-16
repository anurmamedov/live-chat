from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pathlib import Path


def main_view(request):
    return render(request, 'main.html', {})


def serve_css(request):
    css_file_path = Path(__file__).resolve().parent / 'templates/output.css'
    with open(css_file_path, 'r') as f:
        return HttpResponse(f.read(), content_type='text/css')
    

def Check_Username(request):
   print("1")
   return

def my_view(request):
    print('1')
    data = {
        'message': 'Hello from the Krasnovodsk!'
    }
    return JsonResponse(data)