import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()
    director = models.CharField(max_length=127)
    writer = models.CharField(max_length=127)
    actor1 = models.CharField(max_length=127)
    actor2 = models.CharField(max_length=127)
    actor3 = models.CharField(max_length=127)
    runningMinutes = models.IntegerField()
    releaseDate = models.DateField()


class Post(models.Model):
    author = models.ForeignKey(User)
    date = models.DateTimeField()
    rating = models.IntegerField()
    movie = models.ForeignKey(Movie)
    review = models.TextField()


class Like(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    date = models.DateTimeField(default=datetime.datetime.now)


class Comment(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    date = models.DateTimeField(default=datetime.datetime.now)
