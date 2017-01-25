from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from twitter.models import Tweet, Favorite
from django.contrib.auth.models import User
from twitter.forms import *


@login_required
def index(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.save()
            return redirect('twitter:index')
    else:
        form = TweetForm()

    tweets = Tweet.objects.select_related().all().order_by('-id')
    return render(request,
        'twitter/index.html',
        dict(tweets=tweets, form=form)
    )
