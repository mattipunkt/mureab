from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="Startseite"),
    path("addsong/", views.addSong, name="addsong"),
    path("addvote/", views.addVote, name="addvote"),
    path("login/", views.sign_in, name="sign_in"),
    path("logout/", views.sign_out, name="sign_out"),
    path("signup/", views.sign_up, name="sign_up"),
]
