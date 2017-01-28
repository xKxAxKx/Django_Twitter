from django.shortcuts import render, redirect, get_object_or_404
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
            tweet.user_id_id = request.user.id
            tweet.save()
            return redirect('twitter:index')
    else:
            form = TweetForm()
    tweets = Tweet.objects.select_related().all().order_by('-id')
    return render(request,
        'twitter/index.html',
        dict(tweets=tweets, form=form)
    )


@login_required
def twi_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    tweet.delete()
    return redirect('twitter:index')
