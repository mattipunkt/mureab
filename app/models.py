from django.db import models
from datetime import date

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=400, default="No Title")
    artist = models.CharField(max_length=400, default="No Artist")
    link = models.CharField(max_length=300, default="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    pub_date = models.CharField(max_length=20, default=date.today())
    

class Vote(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    vote = models.CharField(max_length=20)
    user = models.CharField(max_length=100, default="Max Mustermann")