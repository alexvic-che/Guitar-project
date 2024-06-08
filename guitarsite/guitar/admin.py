from django.contrib import admin
from .models import Sings, Difficulty, Authors


@admin.register(Sings)
class SingsAdmin(admin.ModelAdmin):
    list_display = ["title","time_create","is_published","difficult","author"]
    list_display_links = ["title"]
    list_editable = ["is_published", "difficult" ,"author"]
    list_per_page = 10

@admin.register(Difficulty)
class DifficultyAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_per_page = 10

@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_per_page = 10
