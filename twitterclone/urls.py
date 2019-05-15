"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitterclone.authentication.views import dj_login, create_user, dj_logout
from twitterclone.twitteruser.views import index_login, homepage, user_page, user_list
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.views import tweet_view, tweetid

admin.site.register(Tweet)
admin.site.register(TwitterUser)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('login/', dj_login),
    path('signup/', create_user),
    path('logout/', dj_logout),
    path('tweet/', tweet_view),
    path('user/<username>', user_page),
    path('tweet/<int:id>', tweetid),
    path('user_list/', user_list)
]
