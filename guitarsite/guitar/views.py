from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

from guitar.models import Sings, Difficulty, Authors


def index(request):
    sings = Sings.published.all()[:6]
    context={"sings": sings}
    return render(request, "guitar/index.html", context)

def about(request):
    return render(request, "guitar/about.html", {})

def show_sings(request, difficult_slug=None , author_slug=None ):
    if difficult_slug:

        difficults = Difficulty.objects.all()
        authors = Authors.objects.all()

        difficult = get_object_or_404(Difficulty, slug=difficult_slug)


        sings = Sings.published.filter(difficult_id=difficult.pk)
        context = {
            "sings": sings,
            "difficults": difficults,
            "authors": authors
        }
        return render(request, "guitar/all_sings.html", context)
    elif author_slug:

        difficults = Difficulty.objects.all()
        authors = Authors.objects.all()

        author = get_object_or_404(Authors, slug=author_slug)

        sings = Sings.published.filter(author_id=author.pk)
        context = {
            "sings": sings,
            "difficults": difficults,
            "authors": authors
        }
        return render(request, "guitar/all_sings.html", context)
    else:
        sings = Sings.published.all()
        difficults = Difficulty.objects.all()
        authors = Authors.objects.all()
        context = {
            "sings": sings,
            "difficults": difficults,
            "authors": authors
        }
        return render(request, "guitar/all_sings.html", context)

def show_sing(request, sing_slug):
    sing = get_object_or_404(Sings, slug = sing_slug)

    context = {
        "sing": sing
    }
    return render(request,"guitar/sing.html",context)



def not_found_page(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

