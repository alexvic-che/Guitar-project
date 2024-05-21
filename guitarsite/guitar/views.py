from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return render(request, "guitar/index.html", {})

def about(request):
    return render(request, "guitar/about.html", {})

def not_found_page(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")