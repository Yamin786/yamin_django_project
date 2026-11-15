from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registration_form(UserCreationForm):
    class Meta:
        model = User
        fields = ('username' , 'password1' , 'password2')
        
class login_form(forms.Form):
    username = forms.CharField(
        max_length=150, 
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    ) 
