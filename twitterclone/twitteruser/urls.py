from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.notification.models import Notification
from django.contrib import admin


admin.site.register(Tweet)
admin.site.register(TwitterUser)
admin.site.register(Notification)