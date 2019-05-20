from twitterclone.authentication.forms import LoginForm, SignUpForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from twitterclone.twitteruser.models import TwitterUser
from django.contrib import messages


def dj_login(request):
    global form
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            next = request.GET.get('next', '/')
            username = form.data['username']
            password = form.data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            if next:
                return redirect(next)
            else:
                return redirect('/')
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def create_user(request):
    global form
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            next = request.GET.get('next', '/')
            data = form.cleaned_data
            new_user = User.objects.create_user(data['username'], data['email'], data['password'])
            new_user.save()
            TwitterUser.objects.create(user=new_user, username=data['username'])
            login(request, new_user)
            render(request, 'signup.html')
            if next:
                return redirect(next)
            else:
                return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def dj_logout(request):
    logout(request)
    messages.info(request, 'You have successfully logged out')
    return redirect('/')
