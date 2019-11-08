from django.urls import path
from . import views

urlpatterns = [
  path('developers/', views.developers, name='developers'),
  path('characters/', views.character_list, name='character_list'),
  path('characters/<int:pk>/', views.character_detail, name='character_detail'),
  path('characters/new/', views.character_create, name='character_create'),
  path('characters/<int:pk>/edit/', views.character_edit, name='character_edit'),
  path('characters/<int:pk>/delete/', views.character_delete, name='character_delete'),

  path('api/v1/characters/', views.api_characters)
]