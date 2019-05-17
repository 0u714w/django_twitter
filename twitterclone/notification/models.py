from django.db import models
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.models import Tweet

class Notification(models.Model):
    tweet = models.OneToOneField(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, null=True)
    seen = models.BooleanField(default=False)