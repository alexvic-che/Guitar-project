from django.db import models

class Post(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
