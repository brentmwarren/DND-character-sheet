from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    campaign_name = models.CharField(max_length=100, blank=True)
    experience = models.PositiveIntegerField(default=0, blank=True)
    char_class = models.CharField(max_length=100, blank=True)
    level = models.PositiveIntegerField(default=0, blank=True)
    race = models.CharField(max_length=100, blank=True)
    background = models.CharField(max_length=100, blank=True)
    strength = models.PositiveIntegerField(null=True, blank=True)
    dexterity = models.PositiveIntegerField(null=True, blank=True)
    constitution = models.PositiveIntegerField(null=True, blank=True)
    intelligence = models.PositiveIntegerField(null=True, blank=True)
    wisdom = models.PositiveIntegerField(null=True, blank=True)
    charisma = models.PositiveIntegerField(null=True, blank=True)
    speed = models.PositiveIntegerField(null=True, blank=True)
    armor_class = models.PositiveIntegerField(null=True, blank=True)
    hit_points = models.PositiveIntegerField(null=True, blank=True)
    proficiency_bonus = models.PositiveIntegerField(null=True, blank=True)
    skill_proficiencies = models.TextField(blank=True)
    saving_throws = models.TextField(blank=True)
    alignment = models.CharField(max_length=100, blank=True)
    campaign = models.CharField(max_length=100, default=None)
    image = models.TextField(default="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fthesocietypages.org%2Fsocimages%2Ffiles%2F2009%2F05%2Fnopic_192.gif&f=1&nofb=1")
    slug = models.SlugField(max_length=40)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="characters")

    def __str__(self):
        return self.name
