from django.shortcuts import redirect, render
from twitterclone.tweet.models import Tweet
from twitterclone.tweet.forms import TweetForm
from operator import attrgetter

def tweet_view(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                body=data['body'],
                userprofile=request.user.twitteruser
            )
            render(request, 'submittweet.html')
            return redirect('/')
    else:
        form = TweetForm()

    return render(request, 'submittweet.html', {'form': form})

def tweetid(request, id):
    html = 'tweet.html'
    tweets = Tweet.objects.filter(pk=id)
    return render(request, html, {'tweets': tweets})

def find_following_tweets(user_id, following):
    tweets = Tweet.objects.filter(userprofile=user_id).all()
    my_tweet_count = len(tweets)
    for user in following:
        tweets = tweets | Tweet.objects.filter(userprofile=user.pk).all()
    return {"tweets": sorted(tweets, key=attrgetter('date_created'),
                             reverse=True),
            "tweet_count": my_tweet_count}