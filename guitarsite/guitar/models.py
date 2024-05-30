from django.db import models
from django.urls import reverse

class PublishedModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Sings.Status.PUBLISHED)

class Sings(models.Model):
    class Status(models.TextChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True,db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    difficult = models.ForeignKey("Difficulty", on_delete=models.PROTECT, related_name="sings")
    chords = models.ManyToManyField("Chords", related_name="sings")

    objects = models.Manager()
    published = PublishedModel()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-time_create"]
        indexes = [
            models.Index(fields=["-time_create"]),
        ]

    def get_absolute_url(self):
        return reverse('sing', kwargs={'sing_slug':self.slug})

class Difficulty(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('difficults', kwargs={'difficult_slug':self.slug})

class Chords(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.name