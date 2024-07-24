from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class PublishedModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Songs.Status.PUBLISHED)

class Songs(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=50, verbose_name="Название песни")
    slug = models.SlugField(max_length=255, unique=True,db_index=True)
    content = models.TextField(blank=True, verbose_name="Текст песни")
    card_image = models.ImageField(upload_to="card_images", blank=True, default=None, null=True, verbose_name="Картинка карточки")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x:(bool(x[0]),x[1]),Status.choices)), default=Status.DRAFT, verbose_name="Публикация")
    difficult = models.ForeignKey("Difficulty", on_delete=models.PROTECT, related_name="songs", verbose_name="Сложность")
    chords = models.ManyToManyField("Chords", related_name="songs", verbose_name="Аккорды")
    author = models.ForeignKey("Authors", on_delete=models.PROTECT, related_name="songs", verbose_name="Автор")
    user_author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='songs', null=True, default=None)

    objects = models.Manager()
    published = PublishedModel()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"
        ordering = ["-time_create"]
        indexes = [
            models.Index(fields=["-time_create"]),
        ]

    def get_absolute_url(self):
        return reverse('song', kwargs={'song_slug':self.slug})



class Difficulty(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Сложность")
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Сложность песни"
        verbose_name_plural = "Сложность песен"

    def get_absolute_url(self):
        return reverse('songs_by_difficulty', kwargs={'difficult_slug':self.slug})

class Chords(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Аккорды")
    designation = models.CharField(max_length=100, db_index=True,null=True,default=None, verbose_name="Обозначение")
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    chord_image = models.ImageField(upload_to="chords_images", blank=True, default=None, null=True, verbose_name="Картинка аккорда")
    chords_group = models.ForeignKey("ChordsGroup", on_delete=models.PROTECT, related_name="chords",blank=True, default=None, null=True)

    def __str__(self):
        return self.name
class ChordsGroup(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    group_image = models.ImageField(upload_to="chords_group_images", blank=True, default=None, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chords_by_group', kwargs={'chords_group_slug':self.slug})


class Authors(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Автор")
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    class Meta:
        verbose_name = "Автор песни"
        verbose_name_plural = "Авторы песен"

    def __str__(self):
        return self.name
    def get_absolute_url(self):

        return reverse('songs_by_author', kwargs={'author_slug':self.slug})
