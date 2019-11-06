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