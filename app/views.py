from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


from .models import Song
from .forms import LoginForm, RegisterForm

# Index-View
def index(request):
    songs = Song.objects.order_by("-pub_date")
    title = "Main"
    return render(request, 
                  "index.html", 
                  {
                      "songs": songs, 
                      },
                  )


def addSong(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        link = request.POST.get('link')
        
        song = Song.objects.create(title=title, artist=artist, link=link)
        return HttpResponse("Das hat geklappt!")
    else: return HttpResponse("Das hat nicht geklappt!")
    
# addVote-function to add votes to database
def addVote(request):
    if request.method == 'POST':
        value = request.POST.get('value')
        song_id = request.POST.get('song_id')
        song = get_object_or_404(Song, id=song_id)

        print("addVote called:")
        print('Song-value: ' + value)
        print('SongID: ' + song_id)
        
        # TODO: check, if a song was already voted by user
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


# User-Manager

def sign_in(request): 
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('index')
        

        form = LoginForm()
        return render(request, "login.html", {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, Wilkommen zurück!')
                return redirect('index')
            
        messages.error(request, f'Falscher Nutzername oder Passwort')
        return render(request, "login.html", {'form': form})
    

def sign_out(request):
    logout(request)
    messages.success(request, f'Du hast dich erfolgreich ausgeloggt!')
    return redirect('login')

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save
            messages.success(request, 'Du hast dich erfolgreich registriert!')
            sign_in(request, user)
            return redirect('index')
        else: return render(request, 'register.html', {'form': form})