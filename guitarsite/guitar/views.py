from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from guitar.models import Sings


def index(request):
    sings = Sings.objects.filter(is_published=1)[:6]
    context={"sings": sings}
    return render(request, "guitar/index.html", context)

def about(request):
    return render(request, "guitar/about.html", {})

def show_sings(request):
    sings = Sings.objects.filter(is_published=1)
    context = {"sings": sings}
    return render(request, "guitar/all_sings.html", context)

def show_sing(request, sing_slug):
    sing = get_object_or_404(Sings, slug = sing_slug)
    context = {"sing": sing}
    return render(request,"guitar/sing.html",context)

def not_found_page(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")