from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate


from .forms import LoginUserForm

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('index'))