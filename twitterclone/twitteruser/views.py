from twitterclone.authentication.forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

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

def homepage(request):

    html = 'homepage.html'
    user_info = User

    return render(request, html, {'user_info': user_info})

