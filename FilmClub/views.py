from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'login.html', {
                  'title': "Login"
    })

def register(request):
    return render(request, 'register.html', {
                'title': "Register"
    })