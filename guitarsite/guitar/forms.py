from django import forms
from captcha.fields import CaptchaField

from .models import Songs


class AddSongForm(forms.ModelForm):

    class Meta:
        model = Songs
        fields = ['title','content','card_image','is_published','difficult','chords','author']



class ContactForm(forms.Form):
    name = forms.CharField(label='Имя',max_length=255)
    email = forms.EmailField(label="Email")
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}))
    captcha = CaptchaField()