from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.db import models
from django.utils.translation import ugettext_lazy as _
from .models import User


class DateInput(forms.DateInput):
    input_type = 'date'

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "employee_id", "date_of_birth", "emp_ctc", "manager_name",
                  "date_of_exit", "department", "remarks", "emp_cv", "emp_images",)
        widgets = {
            "email": forms.EmailInput(attrs={'class':'form-control'}),
            "employee_id": forms.NumberInput(attrs={'class':'form-control'}),
            "date_of_birth": forms.DateInput(attrs={'class':'form-control'}),
            "emp_ctc": forms.NumberInput(attrs={'class':'form-control'}),
            "manager_name": forms.TextInput(attrs={'class':'form-control'}),
            "date_of_exit": forms.DateTimeInput(attrs={'class':'form-control'}),
            "department": forms.TextInput(attrs={'class':'form-control'}),
            "remarks": forms.Textarea(attrs={'class':'form-control'}),
            "emp_cv": forms.FileInput(attrs={'class':'form-control'}),
            "emp_images": forms.FileInput(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}),
    )