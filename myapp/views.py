from django.contrib.auth import logout, views as auth_views
# from django.contrib.auth import forms
from django.shortcuts import redirect, render
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LoginForm

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'myapp/signup.html', {'form':fm})


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'myapp/profile.html')
    else:
        return redirect('/login/')

def user_logout(request):
    logout(request)
    return redirect('/login/')

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'myapp/login.html'

# def user_login(request):
#     fm = AuthenticationForm()
#     return render(request, 'myapp/login.html', {'form':fm})