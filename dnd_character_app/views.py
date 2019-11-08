from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

from .models import Character

# Create your views here.

def home(request):
  return HttpResponse("Goodbye rocket ship. Hello Home.")

def api_characters(request):
  all_characters = Character.objects.all()
  data = []
  for character in all_characters:
    data.append({"name": artist.name})
  return JsonResponse({"data":data, "status":200})

def character_list(request):
  characters = Character.objects.all()
  context = {"characters":characters}
  return render(request, 'character_list.html', context)

def character_detail(request,pk):
  character = Character.objects.get(id=pk)
  context = {"character":character}
  return render(request, 'character_detail.html', context)

#the code below is taking into account we are us django forms. If this is not the case, we will ned to re-factore it
@login_required
def character_create(request):
  if request.method == 'POST':
    form = CharacterForm(request.POST)
    if form.is_valid():
      character = form.save(commit=False)
      character.user = request.user
      character.save()
      return redirect('artist_detail', pk=artist.pk)
  else:
    form = CharacterForm()
  context = {'form': form, 'header': "Add New Character"}
  return render(request, 'character_form.html', context)

#the code below is taking into account we are us django forms. If this is not the case, we will ned to re-factore it
@login_required
def character_edit(request, pk):
  character = Character.objects.get(id=pk)
  if request.method == 'POST':
    form = CharacterForm(request.POST, instance=character)
    if form.is_valid():
      artist = form.save()
      return redirect('character_detail', pk=artist.pk)
  else:
    form = CharacterForm(instance=character)
  context = {'form': form, 'header': f"Edit {character.name}"}
  return render(request, 'character_form.html', context)

@login_required
def character_delete(request, pk):
  Character.objects.get(id=pk).delete()
  return redirect('character_list')