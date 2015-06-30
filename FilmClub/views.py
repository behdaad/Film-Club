import random, datetime

from .models import ExtendedUser, Movie, Post, Like, Comment

from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.

def calculate_rating(movie_id):
    movie = Movie.objects.get(id=movie_id)
    reviews = Post.objects.filter(movie=movie)
    sum = 0
    size = len(reviews)
    for r in reviews:
        sum += r.rating
    movie.rating = round(sum / size, 2)
    movie.save()

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
    for i in randoms:
        calculate_rating(all_movies[i].id)

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

def fetch_posts(users):
    posts = []
    for user in users:
        likes = Like.objects.filter(user=user)
        comments = Comment.objects.filter(user=user)
        reviews = Post.objects.filter(author=user)

        for review in reviews:
            review.reason = review.author.display_name + " posted a review."
            posts.append(review)

        for like in likes:
            already_added = False
            for post in posts:
                if like.post == post:
                    post.reason = like.user.display_name + " liked this."
                    post.save()
                    already_added = True
                    break
            if not already_added:
                posts.append(like.post)

        for comment in comments:
            already_added = False
            for post in posts:
                if comment.post == post:
                    post.reason = comment.user.display_name + " commented on this."
                    post.save()
                    already_added = True
                    break
            if not already_added:
                posts.append(comment.post)

            # for like in likes:
            #     if comment.post == like.post:
            #         if comment.date > like.date:
            #             comment.post.reason = comment.user.display_name + " commented on this."
            #             comment.post.save()

    posts.sort(key=lambda x: x.last_event)
    posts.reverse()
    return posts

def main(request, page=1):
    page = int(page)
    if page < 0:
        return HttpResponse("Error")
    if request.user.is_authenticated():
        extended_user = ExtendedUser.objects.filter(user=request.user)[0]
        followings = extended_user.following.all()

        posts = fetch_posts(followings)[(page - 1) * 10: page * 10 + 1]

        for post in posts:
            post.liked = False
            post.save()

        for post in posts:
            for like in post.likes.all():
                if like.user == extended_user:
                    like.post.liked = True
                    like.post.save()
                    break

        has_older = False
        older_page = page - 1
        if page != 1:
            has_older = True

        has_newer = True
        newer_page = page + 1
        if len(posts) != 11:
            has_newer = False

        return render(request, 'timeline.html',
        {
            'title': "Timeline",
            'page': "timeline",
            'posts': posts,
            'has_older': has_older,
            'has_newer': has_newer,
            'older_page': older_page,
            'newer_page': newer_page,
            'movies': suggested_movies(request.user),
            'users': suggested_users(request.user),
            'logged_in': extended_user,
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

@login_required
def logout_user(request):
    logout(request)
    return redirect("/")

@login_required
def follow(request, user_id):
    user_id = int(user_id)
    follower_extended_user = ExtendedUser.objects.filter(user=request.user)[0]
    followed_extended_user = ExtendedUser.objects.filter(id=user_id)[0]

    follower_extended_user.following.add(followed_extended_user)

    # return redirect(request.GET['next'])
    return HttpResponse("OK")

@login_required
def unfollow(request, user_id):
    user_id = int(user_id)
    unfollower_extended_user = ExtendedUser.objects.filter(user=request.user)[0]
    unfollowed_extended_user = ExtendedUser.objects.filter(id=user_id)[0]

    unfollower_extended_user.following.remove(unfollowed_extended_user)

    # return redirect(request.GET['next'])
    return HttpResponse("OK")

@login_required
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
            calculate_rating(m.id)
            movie_results.append(m)

    # print(user_results[0].posts.all())

    return render(request, 'search.html', {
        'title': "Search",
        'movie_results': movie_results,
        'user_results': user_results,
        'movies': suggested_movies(request.user),
        'users': suggested_users(request.user),
        'logged_in': ExtendedUser.objects.filter(user=request.user)[0],
    })

@login_required
def single_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.liked = False
    post.save()

    for like in post.likes.all():
        if like.user == ExtendedUser.objects.get(user=request.user):
            post.liked = True
            post.save()
            break

    return render(request, 'single_post.html', {
        'title': "Single Post",
        'post': post,
        'movies': suggested_movies(request.user),
        'users': suggested_users(request.user),
        'logged_in': ExtendedUser.objects.filter(user=request.user)[0],
    })

@login_required
def show_user(request, user_id):
    target_user = ExtendedUser.objects.get(id=user_id)
    logged_in_extended_user = ExtendedUser.objects.filter(user=request.user)[0]

    posts = Post.objects.filter(author=target_user)
    for post in posts:
        post.liked = False
        post.save()

    for post in posts:
        for like in post.likes.all():
            if like.user == logged_in_extended_user:
                like.post.liked = True
                like.post.save()
                break

    followings_count = len(target_user.following.all())
    followers_count = 0
    all_users = ExtendedUser.objects.all()
    for user in all_users:
        if target_user in user.following.all():
            followers_count += 1

    dictionary = {
        'title': target_user.display_name,
        'user': target_user,
        'logged_in': ExtendedUser.objects.filter(user=request.user)[0],
        'movies': suggested_movies(request.user),
        'users': suggested_users(request.user),
        'posts': posts,
        'followings_count': followings_count,
        'followers_count': followers_count,
    }

    if target_user == logged_in_extended_user:
        return render(request, 'user_profile.html', dictionary)

    followings = logged_in_extended_user.following.all()
    if target_user in followings:
        return render(request, 'following_profile.html', dictionary)
    else:
        return render(request, 'not_following_profile.html', dictionary)

@login_required
def show_followers(request, user_id):
    target_user = ExtendedUser.objects.filter(id=user_id)[0]

    users_list = []
    all_users = ExtendedUser.objects.all()
    for user in all_users:
        if target_user in user.following.all():
            users_list.append(user)
    followings_count = len(target_user.following.all())
    followers_count = 0
    all_users = ExtendedUser.objects.all()
    for user in all_users:
        if target_user in user.following.all():
            followers_count += 1

    return render(request, 'follower_following.html', {
        'title': target_user.display_name + "'s Followers",
        'user': target_user,
        'logged_in': ExtendedUser.objects.filter(user=request.user)[0],
        'movies': suggested_movies(request.user),
        'users': suggested_users(request.user),
        'users_list': users_list,
        'followers': True,
        'followings_count': followings_count,
        'followers_count': followers_count,
    })

@login_required
def show_followings(request, user_id):
    target_user = ExtendedUser.objects.filter(id=user_id)[0]
    users_list = target_user.following.all()

    followings_count = len(target_user.following.all())
    followers_count = 0
    all_users = ExtendedUser.objects.all()
    for user in all_users:
        if target_user in user.following.all():
            followers_count += 1

    return render(request, 'follower_following.html', {
        'title': target_user.display_name + "'s Followers",
        'user': target_user,
        'logged_in': ExtendedUser.objects.filter(user=request.user)[0],
        'movies': suggested_movies(request.user),
        'users': suggested_users(request.user),
        'users_list': users_list,
        'followers': False,
        'followings_count': followings_count,
        'followers_count': followers_count,
    })

@login_required
def show_movie(request, movie_id):
    movie = Movie.objects.filter(id=movie_id)[0]
    calculate_rating(movie.id)

    return render(request, 'filmProfile.html', {
        'title': movie.name,
        'logged_in': ExtendedUser.objects.filter(user=request.user)[0],
        'movies': suggested_movies(request.user),
        'users': suggested_users(request.user),
        'movie': movie,
    })

@login_required
def submit_review(request, movie_id):
    movie = Movie.objects.filter(id=movie_id)[0]

    new_post = Post()
    new_post.author = ExtendedUser.objects.filter(user=request.user)[0]
    new_post.date = datetime.datetime.now()
    new_post.rating = int(request.POST['rating'])
    new_post.movie = movie
    new_post.review = request.POST['review']

    new_post.save()

    return redirect('/movie/' + str(movie_id) + '/reviews/')

@login_required
def show_reviews(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    calculate_rating(movie.id)

    posts = Post.objects.filter(movie=movie).order_by('-date')

    for post in posts:
        post.liked = False
        post.save()

    for post in posts:
        for like in post.likes.all():
            if like.user == ExtendedUser.objects.get(user=request.user):
                like.post.liked = True
                like.post.save()
                break

    return render(request, 'movie_reviews.html', {
        'title': movie.name,
        'logged_in': ExtendedUser.objects.filter(user=request.user)[0],
        'movies': suggested_movies(request.user),
        'users': suggested_users(request.user),
        'movie': movie,
        'posts': posts,
    })

@login_required
def like_post(request, post_id):
    target_post = Post.objects.filter(id=post_id)[0]
    target_post.last_event = datetime.datetime.now()
    target_post.save()

    target_user = ExtendedUser.objects.filter(user=request.user)[0]

    new_like = Like()
    new_like.user = target_user
    new_like.post = target_post
    new_like.date = target_post.last_event

    new_like.save()

    return HttpResponse("OK")

@login_required
def unlike_post(request, post_id):
    target_post = Post.objects.filter(id=post_id)[0]
    target_user = ExtendedUser.objects.filter(user=request.user)[0]
    target_like = Like.objects.filter(post=target_post).filter(user=target_user)

    if len(target_like) == 1:
        target_like.delete()
    else:
        return HttpResponse("Error")

    previous_likes = target_post.likes.all()
    previous_comments = target_post.comments.all()

    if len(previous_likes) == 0 and len(previous_comments) == 0:
        target_post.last_event = target_post.date
        target_post.save()
        return HttpResponse("OK")

    if len(previous_likes) > 0 and len(previous_comments) == 0:
        latest_like_date = target_post.likes.order_by('-date')[0].date
        target_post.last_event = latest_like_date
        target_post.save()
        return HttpResponse("OK")

    if len(previous_comments) > 0 and len(previous_likes) == 0:
        latest_comment_date = target_post.comments.order_by('-date')[0].date
        target_post.last_event = latest_comment_date
        target_post.save()
        return HttpResponse("OK")

    latest_comment_date = target_post.comments.order_by('-date')[0].date
    latest_like_date = target_post.likes.order_by('-date')[0].date

    if latest_comment_date < latest_like_date:
        target_post.last_event = latest_like_date
    else:
        target_post.last_event = latest_comment_date

    target_post.save()

    return HttpResponse("OK")

@login_required
@csrf_exempt
def comment_on_post(request, post_id):
    # print("comment")
    if request.POST['comment_text'] != "":
        target_post = Post.objects.get(id=post_id)
        target_post.last_event = datetime.datetime.now()
        target_post.save()

        new_comment = Comment()
        new_comment.date = target_post.last_event
        new_comment.post = target_post
        new_comment.user = ExtendedUser.objects.get(user=request.user)
        new_comment.text = request.POST['comment_text']

        new_comment.save()

        return HttpResponse("OK")
    else:
        return HttpResponse("Empty comment; not submitted")

