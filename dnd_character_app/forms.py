from django import forms

from .models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = (
            'name',
            'bio',
            'campaign_name',
            'experience',
            'char_class',
            'level',
            'race',
            'strength',
            'dexterity',
            'constitution',
            'intelligence',
            'wisdom',
            'charisma',
            'armor_class',
            'hit_points',
            'proficiency_bonus',
            'alignment',
            'campaign',
            'image',
        )
