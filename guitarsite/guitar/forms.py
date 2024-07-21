from django import forms
from captcha.fields import CaptchaField

from .models import Songs,Difficulty

placeholder_for_content = """I wanna take you somewhere so you know I care
But it's so cold and I don't know where
I brought you daffodils in a pretty string
But they won't flower like they did last spring"""

class AddSongForm(forms.ModelForm):

    class Meta:
        model = Songs
        fields = ['title','content','card_image','is_published','difficult','author','chords']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control",
                                            "placeholder": "Another love"}),
            "content": forms.Textarea(attrs={"class": "form-control",
                                             "placeholder": placeholder_for_content}),
            "card_image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "is_published": forms.CheckboxInput(attrs={"class": "form-check-input",
                                                       "role": "switch"}),
            "difficult": forms.Select(attrs={"class": "form-select"}),
            "author": forms.Select(attrs={"class": "form-select"}),
            "chords": forms.SelectMultiple(attrs={"class": "form-select"})
        }
class EditSongForm(forms.ModelForm):

    class Meta:
        model = Songs
        fields = ['title','content','card_image','is_published','difficult','author','chords']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control",
                                            "placeholder": "Another love"}),
            "content": forms.Textarea(attrs={"class": "form-control",
                                             "placeholder": placeholder_for_content}),
            "card_image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "is_published": forms.CheckboxInput(attrs={"class": "form-check-input",
                                                       "role": "switch"}),
            "difficult": forms.Select(attrs={"class": "form-select"}),
            "author": forms.Select(attrs={"class": "form-select"}),
            "chords": forms.SelectMultiple(attrs={"class": "form-select"})
        }



class ContactForm(forms.Form):
    name = forms.CharField(label='Имя',max_length=255, widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ваше имя"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control", "placeholder":"Ваш Email"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control",'cols':60, 'rows':10, "placeholder":"Ваш текст"}),
                              label="Текст письма")
    captcha = CaptchaField(label="")