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
from twitterclone.authentication.views import Login, create_user, Logout
from twitterclone.twitteruser.views import homepage, user_page, User_list

from twitterclone.tweet.views import tweet_view, TweetId

from twitterclone.notification.views import notification


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('login/', Login.as_view()),
    path('signup/', create_user),
    path('logout/', Logout.as_view(), name="logout"),
    path('tweet/', tweet_view),
    path('user/<username>', user_page),
    path('tweet/<int:id>', TweetId.as_view(), name="tweets"),
    path('user_list/', User_list.as_view(), name="users"),
    path('notification/', notification)
]
