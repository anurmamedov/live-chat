from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authapp:login')  # Redirect to a login or success page
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('main-view') 
    
    
class CustomLogoutView(LogoutView):
    template_name = 'login.html'
    # def get_redirect_url(self):
    #     return reverse_lazy('authapp:login')    
    
