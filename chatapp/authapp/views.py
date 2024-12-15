from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.views import LoginView

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
    # redirect_authenticated_user = True  # Redirect users who are already logged in
    extra_context = {'page_title': 'Login'}
