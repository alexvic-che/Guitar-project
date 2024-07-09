from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.views import View
from django.views.generic import ListView

from .models import Songs, Difficulty, Authors
from .forms import AddSongForm


class Index(ListView):
    template_name = "guitar/index.html"
    context_object_name = "songs"
    allow_empty = False
    def get_queryset(self):
        return Songs.published.all()[:6]

def about(request):
    return render(request, "guitar/about.html", {})



class ShowSongs(ListView):
    template_name = 'guitar/all_songs.html'
    context_object_name = "songs"
    allow_empty = False

    def get_queryset(self):
        queryset = Songs.published.all()
        difficult_slug = self.kwargs.get("difficult_slug")
        author_slug = self.kwargs.get("author_slug")

        if difficult_slug:
            difficult = get_object_or_404(Difficulty, slug=difficult_slug)
            queryset = queryset.filter(difficult_id=difficult.pk)
        elif author_slug:
            author = get_object_or_404(Authors, slug=author_slug)
            queryset = queryset.filter(author_id=author.pk)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['difficults'] = Difficulty.objects.all()
        context['authors'] = Authors.objects.all()

        difficult_slug = self.kwargs.get("difficult_slug")
        author_slug = self.kwargs.get("author_slug")

        if difficult_slug:
            context['difficult'] = get_object_or_404(Difficulty, slug=difficult_slug)
        elif author_slug:
            context['author'] = get_object_or_404(Authors, slug=author_slug)

        return context



def show_song(request, song_slug):
    song = get_object_or_404(Songs, slug = song_slug)

    context = {
        "song": song
    }
    return render(request,"guitar/song.html",context)

# class ShowSong(ListView):
#     template_name = "guitar/song.html"
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context[]

class AddSong(View):
    def get(self, request):
        form = AddSongForm()
        context = {
            "form": form
        }

        return render(request, "guitar/add_song.html", context)
    def post(self, request):
        form = AddSongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
        context = {
            "form": form
        }

        return render(request, "guitar/add_song.html", context)




def not_found_page(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

