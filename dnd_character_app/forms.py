from django import forms

from .models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = (
            'name',
            'image',
        )


class CharacterEditForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = (
            'notes',
            'experience',
            'char_class',
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
            'alignment',
            'level',
            'skill_proficiencies',
            'saving_throws',
            'proficiency_bonus',
        )
