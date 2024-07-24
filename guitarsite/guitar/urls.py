from django.urls import path, re_path
from . import views

urlpatterns = [

    path("", views.Index.as_view(), name="index"),
    path("about/",views.about, name = "about"),
    path("song/<slug:song_slug>/", views.ShowSong.as_view(), name="song"),
    path("songs/", views.ShowSongs.as_view(), name="songs"),
    path('songs/user_songs/<int:user_author_id>/', views.ShowUserSongs.as_view(), name='user_songs'),
    path("songs/difficult/<slug:difficult_slug>/", views.ShowSongs.as_view(), name="songs_by_difficulty"),
    path("songs/author/<slug:author_slug>/", views.ShowSongs.as_view(), name="songs_by_author"),
    path("add_song/", views.AddSong.as_view(), name="add_song"),
    path("update_song/<slug:slug>/", views.UpdateSong.as_view(), name="update_song"),
    path("delete_song/<slug:slug>/", views.DeleteSong.as_view(), name="delete_song"),
    path("contact/", views.ContactFormView.as_view(), name='contact'),
    path("chords/", views.ShowAllChordsGroup.as_view(), name='chords'),
    path("chords/<slug:chords_group_slug>/", views.ShowChordsByGroup.as_view(), name='chords_by_group'),

]

