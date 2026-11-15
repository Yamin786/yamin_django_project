from django.shortcuts import render , redirect
from .forms import registerForm , loginForm
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def registerView(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = registerForm()
    return render(request , 'register.html' , {'form':form})


def loginView(request):
    if request.method == 'POST':
        form = loginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect('home')

    else:
        form = loginForm()

    return render(request, 'login.html', {'form': form})



@login_required(login_url='login')
def homeView(request):
    return render(request,'home.html')


def logoutView(request):
    logout(request)
    return redirect('login')