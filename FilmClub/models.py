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
    excerpt = models.CharField(max_length=255)
    genre = models.CharField(max_length=127)
    director = models.ForeignKey(Person, related_name="director")
    writer = models.ForeignKey(Person, related_name="writer")
    actor1 = models.ForeignKey(Person, related_name="actor1")
    actor2 = models.ForeignKey(Person, related_name="actor2")
    runningMinutes = models.IntegerField()
    releaseDate = models.DateField()
    poster = models.CharField(max_length=127)  # including the extension
    rating = models.FloatField()
    rating_calculation_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name

class ExtendedUser(models.Model):
    user = models.OneToOneField(User)
    display_name = models.CharField(max_length=127)
    birthday = models.DateField()
    gender = models.CharField(max_length=10)
    following = models.ManyToManyField('self', symmetrical=False, blank=True)
    has_avatar = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey(ExtendedUser)
    date = models.DateTimeField()
    rating = models.IntegerField()
    movie = models.ForeignKey(Movie)
    review = models.TextField()

    def __str__(self):
        return str(self.author) + ' (' + str(self.movie) + ')'


class Like(models.Model):
    user = models.ForeignKey(ExtendedUser)
    post = models.ForeignKey(Post)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.user) + " liked " + str(self.post)


class Comment(models.Model):
    user = models.ForeignKey(ExtendedUser)
    post = models.ForeignKey(Post)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.user) + " commented on " + str(self.post)


