from twitterclone.authentication.forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required


@login_required()
def index_login(request):

    html = 'index.html'

    global form
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            password = form.data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/homepage')
    form = LoginForm()
    return render(request, html, {'form': form})

@login_required()
def homepage(request):

    users = list(request.user.twitteruser.following.all())
    current_user = request.user.twitteruser
    users.append(current_user)

    html = 'homepage.html'
    posts_followers = Tweet.objects.filter(
        userprofile__in=users)
    posts = Tweet.objects.filter(userprofile__id=request.user.id)
    tweets = posts.union(posts_followers).order_by('datetime').reverse()
    return render(request, html, {'tweets': tweets})

def user_list(request):
    html = 'user_list.html'
    users = TwitterUser.objects.all()
    return render(request, html, {'users': users})


def user_page(request, username):
    html = 'user.html'
    user = TwitterUser.objects.filter(username=username).first()
    tweets = Tweet.objects.filter(userprofile=user)
    following = user.following.all()
    current_user_follows = TwitterUser.objects.filter(
        user=request.user).first().following.all()


    if request.method == "POST":
        rule = request.POST.get('rule')
        current_user = TwitterUser.objects.filter(user=request.user).first()
        user_id = request.POST.get('id')
        user = TwitterUser.objects.filter(id=user_id).first()
        if rule == "follow":
            current_user.following.add(user.id)
        elif rule == "unfollow":
            current_user.following.remove(user.id)
        return redirect('/user/' + user.username)



    return render(request, html, {"user": user, "following": len(following), "tweets": tweets, "tweet_count": len(tweets), "already_following": True if user in current_user_follows else False, "is_self": True if user.user == request.user else False})




