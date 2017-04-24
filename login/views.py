from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_present = authenticate(request, username=username, password=password)
        if user_present is None:
            user = User(username=username, email=email)
            user.set_password(password)
            user.email_user("Successful Registration", "Thanks for signing up. Have a great day :)", from_email="anusha91rao@gmail.com")
            user.save()
            user_registered_present = authenticate(username=username, password=password)
            login(request, user_registered_present)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'message':'User is already registered / Please Login'})

        
    else:
        return render(request, 'login.html', 'Details entered are invalid')

def login_view(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html', {'username': user.username})
        else:
            return render(request, 'login.html', {'message':'User is not registered'})
    else:
        return render(request, 'login.html', {'message':'Error Logging in the user'})


def logout_view(request):
    logout(request)
    return render(request, 'index.html')
