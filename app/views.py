from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from collections import defaultdict


from .models import Song
from .models import Vote

# Create your views here.
def index(request):
    songs = Song.objects.order_by("-pub_date")
    song_votes_counts = []

    for song in songs:
        votes = Vote.objects.filter(song=song)
        votes_count = {
            'song': song,
            'for_count': votes.filter(vote='FOR').count(),
            'against_count': votes.filter(vote='AGAINST').count(),
            'night_count': votes.filter(vote='NIGHT').count(),
            'abstain_count': votes.filter(vote='ABSTAIN').count(),
        }
        song_votes_counts.append(votes_count)

    
    return render(request, 
                  "index.html", 
                  {
                      "songs": songs, 
                      "song_votes_counts": song_votes_counts,
                      }
                  )


def addSong(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        link = request.POST.get('link')
        
        song = Song.objects.create(title=title, artist=artist, link=link)
        return HttpResponse("Das hat geklappt!")
    else: return HttpResponse("Das hat nicht geklappt!")
    
def addVote(request):
    if request.method == 'POST':
        vote = request.POST.get('value')
        song_id = request.POST.get('song_id')
        song = get_object_or_404(Song, pk=song_id)
        
        vote = Vote.objects.create(song=song, vote=vote)
        return HttpResponse("Das hat geklappt!")
    else: return HttpResponse("Das hat nicht geklappt!")