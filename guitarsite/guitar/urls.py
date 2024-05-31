from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/",views.about, name = "about"),
    path("sing/<slug:sing_slug>/", views.show_sing, name="sing"),
    path("sings/", views.show_sings, name="sings"),

    path("sings/difficult/<slug:difficult_slug>/", views.show_sings, name="sings_by_difficulty"),
    path("sings/author/<slug:author_slug>/", views.show_sings, name="sings_by_author"),

]

