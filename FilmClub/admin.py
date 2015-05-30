from django.contrib import admin

# Register your models here.
from .models import Movie, Post, Like, Comment, ExtendedUser

admin.site.register(Movie)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(ExtendedUser)
