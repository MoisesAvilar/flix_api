from django.db import models

from actors.models import Actor
from genres.models import Genre


class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT, related_name='movies'
    )
    release_date = models.DateField(blank=True, null=True)
    actors = models.ManyToManyField(Actor, related_name='movies')
    resume = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
