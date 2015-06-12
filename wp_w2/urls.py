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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'FilmClub.views.main'),
    url(r'^follow/user/(?P<user_id>\d+)/', 'FilmClub.views.follow'),
    url(r'^unfollow/user/(?P<user_id>\d+)/', 'FilmClub.views.unfollow'),
    url(r'^register/', 'FilmClub.views.register'),
    url(r'^login/', 'FilmClub.views.sign_in'),
    url(r'^logout/', 'FilmClub.views.logout_user'),
    url(r'^search/', 'FilmClub.views.search'),
    url(r'^post/(?P<post_id>\d+)', 'FilmClub.views.single_post'),
    url(r'^user/(?P<user_id>\d+)', 'FilmClub.views.show_user'),
    url(r'^user/(?P<user_id>\d+)/followers', 'FilmClub.views.show_followers'),
    url(r'^user/(?P<user_id>\d+)/following', 'FilmClub.views.show_followings'),

]

# url(r'^blog/(?P<blog_id>\d+)/comment/$', 'blog.views.blog_comment'),
