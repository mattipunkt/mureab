from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addsong/", views.addSong, name="addsong"),
    path("addvote/", views.addVote, name="addvote"),
]
