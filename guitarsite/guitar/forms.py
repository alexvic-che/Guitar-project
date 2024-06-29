from django import forms
from .models import Difficulty, Authors, Chords

class AddSingForm(forms.Form):

    title = forms.CharField(max_length=255)
    slug = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea())
    is_published = forms.BooleanField(required=False)
    author = forms.ModelChoiceField(queryset=Authors.objects.all())
    difficult = forms.ModelChoiceField(queryset=Difficulty.objects.all())
    chords = forms.ModelChoiceField(queryset=Chords.objects.all())
