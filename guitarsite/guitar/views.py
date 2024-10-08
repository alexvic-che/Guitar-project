from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import get_user_model
from transliterate import slugify, translit
import string



from .models import Songs, Difficulty, Authors, Chords, ChordsGroup
from .forms import AddSongForm, ContactForm, EditSongForm, FavoriteForm
from .utils import UserIsAuthorMixin

class Index(ListView):
    template_name = "guitar/index.html"
    context_object_name = "songs"

    def get_queryset(self):
        return Songs.published.all()[:6]

def about(request):
    return render(request, "guitar/about.html", {})



class ShowSongs(ListView):
    template_name = 'guitar/all_songs.html'
    context_object_name = "songs"
    paginate_by = 6

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

class ShowUserSongs(ListView):
    template_name = 'guitar/user_songs.html'
    context_object_name = "songs"
    paginate_by = 6
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['user_author'] = get_user_model().objects.filter(pk=self.kwargs['user_author_id'])[0]
        return context

    def get_queryset(self):
        user = get_user_model().objects.filter(pk=self.kwargs['user_author_id'])[0]
        queryset = Songs.published.filter(user_author=user)
        return queryset


class ShowSong(DetailView):
    model = Songs
    template_name = "guitar/song.html"
    slug_url_kwarg = 'song_slug'
    context_object_name = 'song'

    def get_object(self, queryset=None):
        return get_object_or_404(Songs.published, slug = self.kwargs[self.slug_url_kwarg])


class AddSong(PermissionRequiredMixin,LoginRequiredMixin, CreateView):
    template_name = "guitar/add_song.html"
    form_class = AddSongForm
    success_url = reverse_lazy('index')
    extra_context = {
        "add": 1
    }
    login_url = 'users:login'
    permission_required = 'guitar.add_songs'

    def form_valid(self, form):
        w = form.save(commit=False)
        w.user_author = self.request.user
        tit = w.title
        if tit[0] in string.ascii_letters:
            tit = translit(tit, 'ru')
        w.slug = slugify(f'{tit}')
        return super().form_valid(form)

class UpdateSong(UserIsAuthorMixin,PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    form_class = EditSongForm
    model = Songs
    success_url = reverse_lazy('index')
    template_name = "guitar/add_song.html"
    extra_context = {
        "update":1
    }
    login_url = 'users:login'
    permission_required = 'guitar.change_songs'

class DeleteSong(UserIsAuthorMixin,PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Songs
    success_url = reverse_lazy('index')
    template_name = "guitar/add_song.html"
    extra_context = {
        "delete": 1
    }
    login_url = 'users:login'
    permission_required = 'guitar.delete_songs'

class ContactFormView(LoginRequiredMixin, FormView):
    form_class = ContactForm
    template_name = "guitar/contact.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ShowAllChordsGroup(ListView):
    template_name = 'guitar/all_chords.html'
    context_object_name = "groups"


    def get_queryset(self):
        queryset = ChordsGroup.objects.all()
        return queryset
class ShowChordsByGroup(ListView):
    template_name = 'guitar/chords_by_group.html'
    context_object_name = "chords"

    def get_queryset(self):
        queryset = Chords.objects.filter(chords_group__slug=self.kwargs["chords_group_slug"])
        return queryset

class ShowFavouritesSongs(LoginRequiredMixin, ListView):
    template_name = 'guitar/favorites.html'
    context_object_name = "songs"

    def get_queryset(self):
        queryset = self.request.user.favorite_songs.all()
        return queryset

class AddToFavoritesView(LoginRequiredMixin, View):
    def post(self, request):
        form = FavoriteForm(request.POST)
        if form.is_valid():
            song = get_object_or_404(Songs, id=form.cleaned_data['song_id'])
            request.user.favorite_songs.add(song)
        return redirect(request.META.get('HTTP_REFERER', 'song_list'))
class DelteFromFavoritesView(LoginRequiredMixin, View):
    def post(self, request):
        form = FavoriteForm(request.POST)
        if form.is_valid():
            song = get_object_or_404(Songs, id=form.cleaned_data['song_id'])
            request.user.favorite_songs.remove(song)
        return redirect(request.META.get('HTTP_REFERER', 'song_list'))
def not_found_page(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")



