from django import forms
from .models import Songs

class AddSongForm(forms.ModelForm):

    class Meta:
        model = Songs
        fields = ['title','content','card_image','is_published','difficult','chords','author']




