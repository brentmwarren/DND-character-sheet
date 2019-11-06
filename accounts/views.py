from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

from dnd_character_app import Character

# Create your views here.

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                context = {
                    'error': 'Username is already taken.',
                }
                return render(request, 'landing.html', context)
            else:
                if User.objects.filter(email=email).exists():
                    context = {
                        'error': 'That email already exists.',
                    }
                    return render(request, 'landing.html', context)
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    user.save()
                    return redirect('profile')
        else:
            context = {
                'error': 'Passwords do not match.',
            }
            return render(request, 'landing.html', context)
    else:
        return render(request, 'landing.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            username=username,
            password=password
        )
        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            context = {
                'error': 'Invalid credentials.',
            }
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('signup')
