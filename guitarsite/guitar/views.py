from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "guitar/index.html", {})

def about(request):
    return render(request, "guitar/about.html", {})
