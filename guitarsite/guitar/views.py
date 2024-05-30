from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from guitar.models import Sings, Difficulty


def index(request):
    sings = Sings.published.all()[:6]
    context={"sings": sings}
    return render(request, "guitar/index.html", context)

def about(request):
    return render(request, "guitar/about.html", {})

def show_sings(request):
    sings = Sings.published.all()
    difficults = Difficulty.objects.all()
    context = {
        "sings": sings,
        "difficults": difficults
    }
    return render(request, "guitar/all_sings.html", context)

def show_sing(request, sing_slug):
    sing = get_object_or_404(Sings, slug = sing_slug)

    context = {
        "sing": sing
    }
    return render(request,"guitar/sing.html",context)

def show_sings_by_difficult(request, difficult_slug):
    difficults = Difficulty.objects.all()
    difficult = get_object_or_404(Difficulty, slug=difficult_slug)
    sings = Sings.published.filter(difficult_id = difficult.pk)

    context = {
        "difficults": difficults,
        "difficult": difficult,
        "sings":sings,
               }
    return render(request,"guitar/all_sings.html", context)

def not_found_page(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
