from django import forms
from .models import Sings

class AddSingForm(forms.ModelForm):
    class Meta:
        model = Sings
        fields = ['title','slug','content','is_published','difficult','chords','author']
        labels={'slug':"URL"}



