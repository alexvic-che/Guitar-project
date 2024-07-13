from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.views.generic import CreateView
from django.contrib.auth import get_user_model


from .forms import LoginUserForm, RegisterUserForm

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('index'))

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:register_done')

def register_done(request):
    reg_user = get_user_model().objects.latest('id')
    return render(request, 'users/register_done.html', context={'reg_user': reg_user})


