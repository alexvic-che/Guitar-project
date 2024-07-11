from django.shortcuts import render
from django.http import HttpResponse
def login_user(request):
    return HttpResponse("Login")
def logout_user(request):
    return HttpResponse("Logout")