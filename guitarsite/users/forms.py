from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm


class LoginUserForm(AuthenticationForm):
    username= forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "form-control",
                                            "placeholder": "Ваш ник"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control",
                                            "placeholder": "Ваш пароль"}))

    class Meta:
        model = get_user_model()
        fields = ["username","password"]


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Логин', widget=forms.TextInput(attrs={"class": "form-control",
                                            "placeholder": "Ваш ник"}))
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={"class": "form-control",
                                            "placeholder": "Ваш пароль"}), label='Пароль')
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={"class": "form-control",
                                            "placeholder": "Повтор пароля"}), label='Повтор пароля')

    class Meta:
        model = get_user_model()
        fields = ['username','password1', 'password2','email','first_name', 'last_name']
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control",
                                            "placeholder": "Email"}),
            "first_name": forms.TextInput(attrs={"class": "form-control",
                                            "placeholder": "Вашe имя"}),
            "last_name": forms.TextInput(attrs={"class": "form-control",
                                                 "placeholder": "Ваша фамилия"}),
        }

    def clean_email(self):
        if get_user_model().objects.filter(email=self.cleaned_data['email']):
            raise forms.ValidationError("Пользователь с таким email уже зарегестрирован")
        else:
            return self.cleaned_data['email']

class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={"class": "form-control",
                                                                                        "placeholder": "Ваш ник"}))
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.EmailInput(attrs={"class": "form-control",
                                                                                        "placeholder": "Ваш email"}))

    class Meta:
        model = get_user_model()
        fields = ['photo','username', 'email', 'first_name', 'last_name']
        widgets = {
            "photo": forms.ClearableFileInput(attrs={"class": "form-control"}),

            "first_name": forms.TextInput(attrs={"class": "form-control",
                                            "placeholder": "Ваш ник"}),
            "last_name": forms.TextInput(attrs={"class": "form-control",
                                            "placeholder": "Ваш ник"}),
        }
        labels = {
            "photo":""
        }

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={"class": "form-control",
                                            "placeholder": "Старый пароль"}))
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={"class": "form-control",
                                            "placeholder": "Новый пароль"}))
    new_password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={"class": "form-control",
                                            "placeholder": "Повтор пароля"}))

