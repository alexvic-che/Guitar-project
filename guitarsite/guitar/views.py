from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify
from django.views import View
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

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


class ShowSong(DetailView):
    model = Songs
    template_name = "guitar/song.html"
    slug_url_kwarg = 'song_slug'
    context_object_name = 'song'

    def get_object(self, queryset=None):
        return get_object_or_404(Songs.published, slug = self.kwargs[self.slug_url_kwarg])


class AddSong(CreateView):
    template_name = "guitar/add_song.html"
    form_class = AddSongForm
    success_url = reverse_lazy('index')
    extra_context = {
        "add": 1
    }

class UpdateSong(UpdateView):
    model = Songs
    fields = ['title','slug','content','card_image','is_published','difficult','chords','author']
    success_url = reverse_lazy('index')
    template_name = "guitar/add_song.html"
    extra_context = {
        "update":1
    }

class DeleteSong(DeleteView):
    model = Songs
    success_url = reverse_lazy('index')
    template_name = "guitar/add_song.html"
    extra_context = {
        "delete": 1
    }






def not_found_page(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

