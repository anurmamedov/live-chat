from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pathlib import Path
from django.contrib.auth.models import User
from .models import Message
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


def main_view(request):
    users = User.objects.all()
    all_messages = Message.objects.all()
    return render(request, 'main.html', {
        'users': users,
        'messages': all_messages,
    })

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            username = body.get('username', '').strip()
            content = body.get('content', '').strip()
            print(username)
            print(content)

            if not username or not content:
                return JsonResponse({'error': 'Invalid data'}, status=400)

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return JsonResponse({'error': 'User does not exist'}, status=404)

            new_message = Message.objects.create(sender=user, content=content)
            return JsonResponse({'success': True, 'message': 'Message sent'}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


def serve_css(request):
    css_file_path = Path(__file__).resolve().parent / 'templates/output.css'
    with open(css_file_path, 'r') as f:
        return HttpResponse(f.read(), content_type='text/css')
    