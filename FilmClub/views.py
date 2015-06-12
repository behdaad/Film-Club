import random

from .models import ExtendedUser, Movie, Post, Like, Comment

from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def suggested_movies(user):
    #  update ratings of movies to suggest
    #  don't forget .save()
    #  also, should check if user has already written a review for the movie
    size = len(Movie.objects.all())
    randoms = [0, 0, 0]
    randoms[0] = random.randint(0, size - 1)

    temp = random.randint(0, size - 1)
    while temp == randoms[0]:
        temp = random.randint(0, size - 1)
    randoms[1] = temp

    temp = random.randint(0, size - 1)
    while temp == randoms[0] or temp == randoms[1]:
        temp = random.randint(0, size - 1)
    randoms[2] = temp

    # randoms contains 3 different random numbers

    all_movies = Movie.objects.all()
    return [all_movies[randoms[0]], all_movies[randoms[1]], all_movies[randoms[2]]]

def suggested_users(user):
    size = len(ExtendedUser.objects.all())
    extended_user = ExtendedUser.objects.filter(user=user)[0]
    all_users = ExtendedUser.objects.all()
    user_id = extended_user.id
    following_count = len(extended_user.following.all())

    if following_count == size - 1:  # user is following everyone
        return []

    randoms = [0, 0, 0]

    temp = random.randint(0, size - 1)
    while all_users[temp] in extended_user.following.all() or temp + 1 == user_id:
        temp = random.randint(0, size - 1)
    randoms[0] = temp
    if following_count == size - 2:  # the only not followed user is found
        return [all_users[randoms[0]]]

    temp = random.randint(0, size - 1)
    while temp == randoms[0] or all_users[temp] in extended_user.following.all() or temp + 1 == user_id:
        temp = random.randint(0, size - 1)
    randoms[1] = temp
    if following_count == size - 3:  # the only 2 not followed users are found
        return [all_users[randoms[0]], all_users[randoms[1]]]

    temp = random.randint(0, size - 1)
    while temp == randoms[0] or temp == randoms[1] or all_users[temp] in extended_user.following.all() or temp + 1 == user_id:
        temp = random.randint(0, size - 1)
    randoms[2] = temp

    return [all_users[randoms[0]], all_users[randoms[1]], all_users[randoms[2]]]

def main(request):
    if request.user.is_authenticated():
        extended_user = ExtendedUser.objects.filter(user=request.user)[0]
        followings = extended_user.following.all()

        posts = []
        for user in followings:
            likes = Like.objects.filter(user=user)
            comments = Comment.objects.filter(user=user)
            reviews = Post.objects.filter(author=user)

            for like in likes:
                posts.append(like.post)
            for comment in comments:
                posts.append(comment.post)
            for review in reviews:
                posts.append(review)

        posts.sort(key=lambda x: x.date)
        # headlines = []
        # for post in posts:
        #     headlines.append()

        return render(request, 'timeline.html', {
            'title': "Timeline",
            'page': "timeline",
            'posts': posts,
            'movies': suggested_movies(request.user),
            'users': suggested_users(request.user),
        })
    else:
        return render(request, 'login.html', {
            'title': "Login"
        })


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class ExtendedUserForm(forms.ModelForm):
    class Meta:
        model = ExtendedUser
        exclude = ['user', 'following', 'gender']

    # gender = forms.ChoiceField(choices=

def register(request):
    if request.method == 'GET':
        user_form = UserForm(prefix="user")
        extended_user_form = ExtendedUserForm(prefix="extended_user")
        return render(request, 'register.html', {
            'title': "Register",
            'form1': user_form,
            'form2': extended_user_form,
        })
    else:  # POST
        # username = request.POST['username']
        # password1 = request.POST['password1']
        # password2 = request.POST['password2']
        # firstName = request.POST['firstName']
        # lastName = request.POST['lastName']
        # date = request.POST['date']
        # gender = request.POST['gender']
        # displayName = request.POST['displayName']
        # email = request.POST['email']

        #  validate form info

        # new_user = User(username=username, password=password1, email=email, first_name=firstName, last_name=lastName)
        # new_user.save()

        # new_extended_user = ExtendedUser(user=new_user, displayName=displayName, birthday=date, isMale=gender)
        # new_extended_user.save()

        return render(request, 'login.html', {
            'title': 'Welcome',
            'error': False,
            'forgot': False,
            'sign_up': True,
        })

def sign_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        target_user = ExtendedUser.objects.filter(user=user)[0]
        target_user.is_online = True
        target_user.save()
        return redirect("/")
    else:
        return render(request, 'login.html', {
            'title': 'Welcome',
            'error': True,
            'forgot': False,
            'sign_up': False,
        })

def logout_user(request):
    logout(request)
    return redirect("/")


def follow(request, user_id):
    user_id = int(user_id)
    follower_user = request.user
    follower_extended_user = ExtendedUser.objects.filter(user=follower_user)[0]
    followed_user = User.objects.filter(id=user_id)[0]
    followed_extended_user = ExtendedUser.objects.filter(user=followed_user)[0]

    follower_extended_user.following.add(followed_extended_user)

    return redirect("/")

def search(request):
    query = request.GET['query'].lower()
    extended_users = ExtendedUser.objects.all()
    user_results = []
    for eu in extended_users:
        if query in eu.user.first_name.lower():
            user_results.append(eu)
        elif query in eu.user.last_name.lower():
            user_results.append(eu)
        elif query in eu.user.username.lower():
            user_results.append(eu)

    movies = Movie.objects.all()
    movie_results = []
    for m in movies:
        if query in m.name.lower():
            movie_results.append(m)

    return render(request, 'search.html', {
        'title': "Search",
        'movie_results': movie_results,
        'user_results': user_results,
        'movies': suggested_movies(request.user),
        'users': suggested_users(request.user),
    })