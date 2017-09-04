from django.db import models
from datetime import datetime


# Create your models here.
class Actors(models.Model):
    fullname = models.CharField(max_length=200, null=True)
    dob = models.DateField(max_length=8)
    gender = models.CharField(max_length=10)
    def __str__(self):
        return self.fullname
class Genres(models.Model):
    genre_type = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.genre_type

class Movies(models.Model):
     movie_title = models.CharField(max_length=200, null=True)
     movie_description = models.TextField(max_length=500, null=True)
     movie_rating = models.IntegerField(null=True)
     genre = models.ForeignKey(Genres)
     release_date = models.DateField(max_length=8, null=True )
     movie_review = models.TextField(max_length=500, null=True)
     actors = models.ManyToManyField(Actors)
     logo_url = models.CharField(max_length=100, null=True)
     movie_logo = models.ImageField(null=True)
     def __str__(self):
         return self.movie_title
