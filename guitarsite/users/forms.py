from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class LoginUserForm(AuthenticationForm):
    username=forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ["username","password"]

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Логин')
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput(), label='Пароль')
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput(), label='Повтор пароля')

    class Meta:
        model = get_user_model()
        fields = ['username','password1', 'password2','email','first_name', 'last_name']

    def clean_email(self):
        if get_user_model().objects.filter(email=self.cleaned_data['email']):
            raise forms.ValidationError("Пользователь с таким email уже зарегестрирован")
        else:
            return self.cleaned_data['email']

class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин')
    email = forms.CharField(disabled=True, label='E-mail')

    class Meta:
        model = get_user_model()
        fields = ['photo','username', 'email', 'first_name', 'last_name']

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput())
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput())