from django.shortcuts import render , redirect
from django.contrib.auth import login , logout , authenticate 
from . import forms
from .serializers import accountSerializer
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def error(request):
    return render(request,'error.html')


def registration_view(request):
    if request.method == "POST":
        form = forms.registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            redirect('error')
    else:
        form = forms.registration_form()
    return render(request , 'register.html' , {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = forms.login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username= username , password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
        else:
            return redirect('error')
    else:
        form = forms.login_form()
    return render(request,'login.html' , {'form':form})


def home_view(request):
    return render(request,'home.html')


# views.py
def logout_view(request):
    logout(request)  
    return redirect('login')

  # Redirect to login page after logout



def apiView(request):  
    
    accounts = User.objects.all()
    
    serializer = accountSerializer(accounts, many=True)
    
    
    return JsonResponse(serializer.data, safe=False)
