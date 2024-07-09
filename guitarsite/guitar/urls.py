from django.urls import path, re_path
from . import views

urlpatterns = [

    path("", views.Index.as_view(), name="index"),
    path("about/",views.about, name = "about"),
    path("song/<slug:song_slug>/", views.show_song, name="song"),
    path("songs/", views.ShowSongs.as_view(), name="songs"),

    path("songs/difficult/<slug:difficult_slug>/", views.ShowSongs.as_view(), name="songs_by_difficulty"),
    path("songs/author/<slug:author_slug>/", views.ShowSongs.as_view(), name="songs_by_author"),
    path("add_song/", views.AddSong.as_view(), name="add_song"),

]

