from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.http import JsonResponse
from .forms import CustomUserCreationForm 


User = get_user_model()

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        avatar = request.FILES.get('avatar')

        # Validate the passwords
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('authapp:register')

        # Create the user
        try:
            user = User.objects.create_user(username=username, email=email, password=password1, avatar=avatar)
            user.save()
            messages.success(request, "Registration successful")
            return redirect('authapp:login')  # Redirect to the login page after successful registration
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect('authapp:register')
    return render(request, 'register.html')  # Your registration form template



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('main-view')  # Redirect to the main view or dashboard
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('authapp:login')  # Stay on the login page if authentication fails

    return render(request, 'login.html')
    
    
class CustomLogoutView(LogoutView):
    template_name = 'login.html'
    # def get_redirect_url(self):
    #     return reverse_lazy('authapp:login')    
    
