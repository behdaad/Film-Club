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
    poster = models.ImageField(upload_to='posters/', default='default_poster.jpg')  # including the extension
    rating = models.FloatField()
    # rating_calculation_date = models.DateTimeField(default=datetime.datetime.now)
    imdb_link = models.CharField(max_length=127)

    def __str__(self):
        return self.name

class ExtendedUser(models.Model):
    user = models.OneToOneField(User)
    display_name = models.CharField(max_length=127)
    birthday = models.DateField(null=True)
    gender = models.CharField(max_length=10)
    following = models.ManyToManyField('self', symmetrical=False, blank=True)
    # has_avatar = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', default="default_avatar.png")
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey(ExtendedUser, related_name="posts")
    date = models.DateTimeField(default=datetime.datetime.now)
    last_event = models.DateTimeField(default=datetime.datetime.now)
    rating = models.IntegerField()
    movie = models.ForeignKey(Movie)
    review = models.TextField()
    liked = models.BooleanField(default=False)  # liked by CURRENT LOGGED IN  USER
    reason = models.CharField(default="", max_length=255)

    def __str__(self):
        return str(self.author) + ' (' + str(self.movie) + ')'

class Like(models.Model):
    user = models.ForeignKey(ExtendedUser)
    post = models.ForeignKey(Post, related_name="likes")
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.user) + " liked " + str(self.post)


class Comment(models.Model):
    class Meta:
        ordering = ['-date']
    user = models.ForeignKey(ExtendedUser)
    post = models.ForeignKey(Post, related_name="comments")
    date = models.DateTimeField(default=datetime.datetime.now)
    text = models.CharField(default="", max_length=1023)

    def __str__(self):
        return str(self.user) + " commented on " + str(self.post)


class Notification(models.Model):
    user = models.ForeignKey(ExtendedUser)
    date = models.DateTimeField(default=datetime.datetime.now)
    type = models.CharField(max_length=20)  # like (post), follow (user), comment_post (post), comment_comment (post)
    post_id = models.IntegerField()


class FollowTuple(models.Model):
    follower = models.ForeignKey(ExtendedUser, related_name='follower')
    followee = models.ForeignKey(ExtendedUser, related_name='followee')
    date = models.DateTimeField(default=datetime.datetime.now)
