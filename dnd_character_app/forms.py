from django import forms

from .models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = (
            'name',
            'notes',
            'campaign_name',
            'experience',
            'char_class',
            'level',
            'race',
            'background',
            'strength',
            'dexterity',
            'constitution',
            'intelligence',
            'wisdom',
            'charisma',
            'speed',
            'armor_class',
            'hit_points',
            'proficiency_bonus',
            'skill_proficiencies',
            'saving_throws',
            'alignment',
            'campaign',
            'image',
        )
