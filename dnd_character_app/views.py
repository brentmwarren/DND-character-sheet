import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.utils.text import slugify

from .models import Character
from .forms import CharacterForm, CharacterEditForm

# Create your views here.

# from django.views.generic.detail import DetailView
# class PostDetailView(DetailView):
#     model = Post
#     # This file should exist somewhere to render your page
#     template_name = 'your_blog/show_post.html'
#     # Should match the value after ':' from url <slug:the_slug>
#     slug_url_kwarg = 'the_slug'
#     # Should match the name of the slug field on the model 
#     slug_field = 'slug' # DetailView's default value: optional
# post_detail_view = PostDetailView.as_view()

def home(request):
  return HttpResponse("Goodbye rocket ship. Hello Home.")


def developers(request):
    return render(request, 'developers.html')


def api_characters(request):
  all_characters = Character.objects.all()
  data = []
  for character in all_characters:
    data.append({"name": character.name})
  return JsonResponse({
    "data": data,
    },
    status=200
  )


@login_required
def character_list(request):
  characters = Character.objects.all()
  context = {"characters":characters}
  return render(request, 'character_list.html', context)

def character_detail(request,pk):
  character = Character.objects.get(id=pk)
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
    form = CharacterEditForm(json.loads(request.body))
    if form.is_valid():
        data = form.cleaned_data
        Character.objects.filter(pk=pk).update(**data)
        return JsonResponse({}, status=200)
    else:
        return JsonResponse(form.errors.get_json_data(), status=400)


@login_required
def character_delete(request, pk):
  Character.objects.get(id=pk).delete()
  return redirect('character_list')

def slug(self):
  return slugify(self.name)
