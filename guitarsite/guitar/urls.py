from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/",views.about, name = "about"),
    path("sings/", views.show_sings, name="sings"),
    path("sing/<slug:sing_slug>/", views.show_sing, name="sing"),
    path("sings/<slug:difficult_slug>/", views.show_sings_by_difficult, name="difficults"),
]

