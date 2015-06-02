from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def main(request):
    return render(request, 'login.html', {
        'title': "Login"
    })

def register(request):
    return render(request, 'register.html', {
        'title': "Register"
    })

def sign_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return timeline(request)
    else:
        return render(request, 'login.html', {
            'title': 'Welcome',
            'error': True,
            'forgot': False,
            'sign_up': False,
        })

def timeline(request):

    return render(request, 'timeline.html')