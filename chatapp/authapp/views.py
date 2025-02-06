from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login


def signup_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)  # Handle files properly
        if form.is_valid():
            user = form.save(commit=False)
            if 'avatar' in request.FILES:
                user.avatar = request.FILES['avatar']
            user.save()
            login(request, user)
            return redirect('main.html')  # Change 'home' to your actual home view
    else:
        form = RegisterForm()
    
    return render(request, "register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('main-view') 
    
    
class CustomLogoutView(LogoutView):
    template_name = 'login.html'
    # def get_redirect_url(self):
    #     return reverse_lazy('authapp:login')    
    
