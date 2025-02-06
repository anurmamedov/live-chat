from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pathlib import Path
from main.models import CustomUser
from .models import Message
from django.core.serializers import serialize
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


def main_view(request):
    users = CustomUser.objects.all()
    all_messages = Message.objects.all()
    return render(request, 'main.html', {
        'users': users,
        'messages': all_messages,
    })

def display_messages(request):
    all_messages = Message.objects.select_related('sender').values('sender__username', 'content', 'date', 'sender__avatar')
    all_messages_list = list(all_messages)
    return JsonResponse({'data': all_messages_list}, status=200)


@csrf_exempt
def send_message(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            username = body.get('username', '').strip()
            content = body.get('content', '').strip()
            if not username or not content:
                return JsonResponse({'error': 'Invalid data'}, status=400)
            try:
                user = CustomUser.objects.get(username=username)
            except CustomUser.DoesNotExist:
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
    