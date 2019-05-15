from django.db import models
from twitterclone.twitteruser.models import TwitterUser

class Tweet(models.Model):
    body = models.CharField(max_length=140)
    datetime = models.DateTimeField(auto_now_add=True)
    userprofile = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)




