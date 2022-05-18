
from re import T
from django.db import models


class Movie(models.Model):
    Title = models.CharField(max_length=255)
    Year = models.TextField(blank=True)
    Rated = models.TextField(blank=True)
    Released = models.TextField(blank=True)
    Runtime = models.TextField(blank=True)
    Genre = models.TextField(blank=True)
    Director = models.TextField(blank=True)
    Writer = models.TextField(blank=True)
    Actors = models.TextField(blank=True)
    Plot = models.TextField(blank=True)
    Language = models.TextField(blank=True)
    Country  = models.TextField(blank=True)
    Awards  = models.TextField(blank=True)
    Poster = models.TextField(blank=True)
    
    Metascore = models.TextField(blank=True)
    imdbRating =models.TextField(blank=True)
    imdbVotes = models.TextField(blank=True)
    imdbID = models.TextField(blank=True)
    Type = models.TextField(blank=True)
    DVD = models.TextField(blank=True)
    BoxOffice = models.TextField(blank=True)
    Production = models.TextField(blank=True)
    Website = models.TextField(blank=True)
    Response = models.TextField(blank=True)
    Comments = models.ManyToManyField("comments.Comment", related_name="movies", blank =True)