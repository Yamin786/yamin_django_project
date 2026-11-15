from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import loginModel

class registerForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username','first_name','last_name')


class loginForm(forms.ModelForm):
    class Meta:
        model  = loginModel
        fields  = ('username','password')
        widgets = {
            'password': forms.PasswordInput(),
        }
