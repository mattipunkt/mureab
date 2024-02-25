from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from collections import defaultdict


from .models import Song
from .models import Vote

# Create your views here.
def index(request):
    songs = Song.objects.order_by("-pub_date")
    
    return render(request, 
                  "index.html", 
                  {
                      "songs": songs, 
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
        value = request.POST.get('value')
        song_id = request.POST.get('song_id')
        song = get_object_or_404(Song, id=song_id)

        print("addVote called:")
        print('Song-value: ' + value)
        print('SongID: ' + song_id)
        
        if value == 'FOR':
            song.for_votes += 1
            song.save()
            return HttpResponse("FOR-Vote added")
        elif value == 'AGAINST':
            song.against_votes += 1
            song.save()
            return HttpResponse("AGAINST-Vote added")
        elif value == 'NIGHT':
            song.night_votes += 1
            song.save()
            return HttpResponse("NIGHT-Vote added")
        elif value == 'ABSTAIN':
            song.abstain_votes += 1
            song.save()
            return HttpResponse("ABSTAIN-Vote added")
        else: return HttpResponse("Error in POST-Request")

