from twitterclone.authentication.forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required
from twitterclone.tweet.views import find_following_tweets


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

    html = 'homepage.html'
    tweets = Tweet.objects.all()
    return render(request, html, {'tweets': tweets})

def user_page(request, username):
    html = 'user.html'
    user = TwitterUser.objects.filter(username=username).first()
    tweets = Tweet.objects.filter(userprofile=user)
    print(tweets)
    following = request.user.twitteruser.following.all()


    return render(request, html, {"user": user, "following": len(following), "tweets": tweets, "tweet_count": len(tweets)})




