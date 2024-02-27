from django.db import models
from datetime import date

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=400, default="No Title")
    artist = models.CharField(max_length=400, default="No Artist")
    link = models.CharField(max_length=300, default="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    for_votes = models.IntegerField(default=0)
    against_votes = models.IntegerField(default=0)
    night_votes = models.IntegerField(default=0)
    abstain_votes = models.IntegerField(default=0)
    pub_date = models.CharField(max_length=20, default=date.today())
    

class User(models.Model):
    name = models.CharField(max_length=100, default="Max Mustermann")