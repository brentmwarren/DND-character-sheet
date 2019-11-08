from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    campaign_name = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(default=0)
    char_class = models.CharField(max_length=100)
    level = models.PositiveIntegerField(default=0)
    race = models.CharField(max_length=100)
    background = models.CharField(max_length=100)
    strength = models.PositiveIntegerField()
    dexterity = models.PositiveIntegerField()
    constitution = models.PositiveIntegerField()
    intelligence = models.PositiveIntegerField()
    wisdom = models.PositiveIntegerField()
    charisma = models.PositiveIntegerField()
    speed = models.PositiveIntegerField()
    armor_class = models.PositiveIntegerField()
    hit_points = models.PositiveIntegerField()
    proficiency_bonus = models.PositiveIntegerField()
    skill_proficiencies = models.TextField()
    saving_throws = models.TextField()
    alignment = models.CharField(max_length=100)
    campaign = models.CharField(max_length=100, default=None)
    image = models.TextField()
    slug = models.SlugField(max_length=40)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="characters")

    def __str__(self):
        return self.name
