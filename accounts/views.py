import json

from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from dnd_character_app.models import Character

# Create your views here.

@require_http_methods(['POST'])
def signup(request):
    new_user_info = json.loads(request.body)
    username = new_user_info['username']
    email = new_user_info['email']

    errors = {}
    if User.objects.filter(username=username).exists():
        errors['username'] = 'Username is taken'
    if User.objects.filter(email=email).exists():
        errors['email'] = 'Invalid email'

    if not errors:
        new_user_info.pop('password2')
        user = User.objects.create_user(
            **new_user_info,
        )
        user.save()
        auth.login(request, user)
        return JsonResponse({}, status=200)
    else:
        return JsonResponse(errors, status=400)


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
            return redirect('character_list')
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
