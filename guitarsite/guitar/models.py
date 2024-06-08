from django.db import models
from django.urls import reverse

class PublishedModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Sings.Status.PUBLISHED)

class Sings(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=50, verbose_name="Название песни")
    slug = models.SlugField(max_length=255, unique=True,db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x:(bool(x[0]),x[1]),Status.choices)), default=Status.DRAFT, verbose_name="Публикация")
    difficult = models.ForeignKey("Difficulty", on_delete=models.PROTECT, related_name="sings", verbose_name="Сложность")
    chords = models.ManyToManyField("Chords", related_name="sings")
    author = models.ForeignKey("Authors", on_delete=models.PROTECT, related_name="sings", verbose_name="Автор")

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
        return reverse('sing', kwargs={'sing_slug':self.slug})



class Difficulty(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Сложность")
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Сложность песни"
        verbose_name_plural = "Сложность песен"

    def get_absolute_url(self):
        return reverse('sings_by_difficulty', kwargs={'difficult_slug':self.slug})

class Chords(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Аккорды")
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.name

class Authors(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Автор")
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    class Meta:
        verbose_name = "Автор песни"
        verbose_name_plural = "Авторы песен"

    def __str__(self):
        return self.name
    def get_absolute_url(self):

        return reverse('sings_by_author', kwargs={'author_slug':self.slug})
