from django.shortcuts import redirect, render
from twitterclone.tweet.models import Tweet
from twitterclone.tweet.forms import TweetForm

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
            return redirect('/homepage')
    else:
        form = TweetForm()

    return render(request, 'submittweet.html', {'form': form})

def tweetid(request, id):
    html = 'tweet.html'
    tweets = Tweet.objects.filter(pk=id)
    return render(request, html, {'tweets': tweets})