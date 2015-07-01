"""wp_w2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'FilmClub.views.main'),
    url(r'^register/$', 'FilmClub.views.register'),
    url(r'^login/$', 'FilmClub.views.sign_in'),
    url(r'^logout/$', 'FilmClub.views.logout_user'),
    url(r'^search/$', 'FilmClub.views.search'),
    url(r'^timeline/(?P<page>\d+)/$', 'FilmClub.views.main'),

    url(r'^user/(?P<user_id>\d+)/$', 'FilmClub.views.show_user'),
    url(r'^user/(?P<user_id>\d+)/(?P<page>\d+)/$', 'FilmClub.views.show_user'),
    url(r'^user/(?P<user_id>\d+)/follow/$', 'FilmClub.views.follow'),
    url(r'^user/(?P<user_id>\d+)/unfollow/$', 'FilmClub.views.unfollow'),
    url(r'^user/(?P<user_id>\d+)/followers/$', 'FilmClub.views.show_followers'),
    url(r'^user/(?P<user_id>\d+)/following/$', 'FilmClub.views.show_followings'),

    url(r'^movie/(?P<movie_id>\d+)/$', 'FilmClub.views.show_movie'),
    url(r'^movie/(?P<movie_id>\d+)/submit_review/$', 'FilmClub.views.submit_review'),
    url(r'^movie/(?P<movie_id>\d+)/reviews/$', 'FilmClub.views.show_reviews'),
    url(r'^movie/(?P<movie_id>\d+)/reviews/(?P<page>\d+)/$', 'FilmClub.views.show_reviews'),

    url(r'^post/(?P<post_id>\d+)/$', 'FilmClub.views.single_post'),
    url(r'^post/(?P<post_id>\d+)/like/$', 'FilmClub.views.like_post'),
    url(r'^post/(?P<post_id>\d+)/unlike/$', 'FilmClub.views.unlike_post'),
    url(r'^post/(?P<post_id>\d+)/comment/$', 'FilmClub.views.comment_on_post'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# url(r'^blog/(?P<blog_id>\d+)/comment/$', 'blog.views.blog_comment'),
