from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="movies")
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor, related_name="movies")
    resume = models.TextField()

    def __str__(self):
        return self.title + " (" + str(self.release_date.year) + ")"
