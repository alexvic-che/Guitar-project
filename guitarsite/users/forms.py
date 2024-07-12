from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.views import AuthenticationForm
class LoginUserForm(AuthenticationForm):
    username=forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ["username","password"]
