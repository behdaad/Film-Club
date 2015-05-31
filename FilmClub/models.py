import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()
    genre = models.CharField(max_length=127)
    director = models.ForeignKey(Person, related_name="director")
    writer = models.ForeignKey(Person, related_name="writer")
    actor1 = models.ForeignKey(Person, related_name="actor1")
    actor2 = models.ForeignKey(Person, related_name="actor2")
    runningMinutes = models.IntegerField()
    releaseDate = models.DateField()
    poster = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User)
    date = models.DateTimeField()
    rating = models.IntegerField()
    movie = models.ForeignKey(Movie)
    review = models.TextField()

    def __str__(self):
        return self.author + ' (' + self.movie + ')'


class Like(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.user + " liked " + str(self.post)


class Comment(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.user + " commented on " + str(self.post)


class ExtendedUser(models.Model):
    user = models.OneToOneField(User)
    displayName = models.CharField(max_length=127)
    birthday = models.DateField()
    isMale = models.BinaryField()
    following = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.user.username
