from django.db import models
from twitterclone.twitteruser.models import TwitterUser
from datetime import datetime


class Tweet(models.Model):
    body = models.CharField(max_length=140)
    datetime = models.DateTimeField(default=datetime.now, blank=True)
    userprofile = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)




