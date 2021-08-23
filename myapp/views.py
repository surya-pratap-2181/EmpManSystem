from django.contrib.auth import logout, views as auth_views
# from django.contrib.auth import forms
from django.shortcuts import redirect, render
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LoginForm
from .models import User
import datetime

# Create your views here.


def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'myapp/signup.html', {'form': fm})


def age_calculate(date):
    # return (datetime.date.today()-date)/365
    return int((datetime.date.today() - date).days / 365.25)


def profile(request):
    if request.user.is_authenticated:
        dob = request.user.date_of_birth
        age = age_calculate(dob)
        return render(request, 'myapp/profile.html', {'emp': age})
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
