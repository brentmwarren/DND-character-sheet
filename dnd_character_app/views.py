import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.utils.text import slugify

from .models import Character
from .forms import CharacterForm, CharacterEditForm

# Create your views here.

def home(request):
  return render(request, 'landing.html')


def developers(request):
    return render(request, 'developers.html')


@login_required
def character_list(request):
  characters = Character.objects.filter(user=request.user)
  context = {"characters":characters}
  return render(request, 'character_list.html', context)


@login_required
def character_detail(request, pk):
  character = Character.objects.get(id=pk)
  if character.user != request.user:
    raise PermissionDenied
  context = {"character":character}
  return render(request, 'character_detail.html', context)


@login_required
def character_create(request):
  if request.method == 'POST':
    form = CharacterForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      slug = slugify(data['name'])
      character = Character.objects.create(
        **data,
        slug=slug,
        user=request.user
      )
      return redirect('character_detail', pk=character.pk)
    else:
      context = {
        'error': 'Error!',
      }
      return render(request, 'character_form.html', context)
  else:
    form = CharacterForm()
    labels = []
    for field in form.fields.keys():
      label = field.replace('_', ' ').title()
      labels.append(label)

    context = {
      'fields': zip(form.fields.keys(), labels),
      'header': 'Create a character',
    }
    return render(request, 'character_form.html', context)


@login_required
@require_http_methods(['POST'])
def character_edit(request, pk):
    character = Character.objects.get(pk=pk)
    if character.user != request.user:
        raise PermissionDenied
    form = CharacterEditForm(json.loads(request.body))
    if form.is_valid():
        data = form.cleaned_data
        Character.objects.filter(pk=pk).update(**data)
        return JsonResponse(data, status=200)
    else:
        return JsonResponse(form.errors.get_json_data(), status=400)


@login_required
def character_delete(request, pk):
  character = Character.objects.get(pk=pk)
  if character.user != request.user:
      raise PermissionDenied
  character.delete()
  return redirect('character_list')
