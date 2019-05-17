from django.shortcuts import redirect
from twitterclone.twitteruser.models import TwitterUser
from django.shortcuts import redirect, render
from twitterclone.notification.models import Notification
import re

def notification(request):
    html = 'notification.html'
    notifications = request.user.twitteruser.notification_set.get_queryset().all()
    found_notifications = request.user.twitteruser.notification_set
    new_notification = 0
    for notice in found_notifications.get_queryset().all():
        if not notice.seen:
            new_notification += 1
    tweets = []
    for notice in notifications:
        if not notice.seen:
            tweets += [notice.tweet]
            Notification.objects.filter(pk=notice.pk).update(seen=True)
    return render(request, html, {'tweets': tweets, 'notification': new_notification})

def check_for_mentions(tweet):
    notifications = re.findall(r"(@\w+)", tweet.body)
    if notifications:
        for person in notifications:
            user_to_notify = TwitterUser.objects.filter(
                username=person[1:]).first()
            if user_to_notify:
                Notification.objects.create(
                    tweet=tweet,
                    user=user_to_notify
                )
        return redirect('/')


