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
    name = request.POST['name']
    bio = request.POST['bio']
    campaign_name = request.POST['campaign_name']
    experience = request.POST['experience']
    char_class = request.POST['char_class']
    level = request.POST['level']
    race = request.POST['race']
    strength = request.POST['strength']
    dexterity = request.POST['dexterity']
    constitution = request.POST['constitution']
    intelligence = request.POST['intelligence']
    wisdom = request.POST['wisdom']
    charisma = request.POST['charisma']
    armor_class = request.POST['armor_class']
    hit_points = request.POST['hit_points']
    proficiency_bonus = request.POST['proficiency_bonus']
    alignment = request.POST['alignment']
    campaign = request.POST['campaign']
    image = request.POST['image']
    return redirect('character_detail', pk=character.pk)
  else: 
    return render(request, 'create_character.html')
























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