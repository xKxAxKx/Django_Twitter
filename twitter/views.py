from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from twitter.models import Tweet, Favorite
from django.contrib.auth.models import User
from twitter.forms import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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

    tweet_list = Tweet.objects.select_related().all().order_by('-id')

    #ページネーションの設定
    paginator = Paginator(tweet_list, 5)
    page = request.GET.get('page')
    try:
        tweets = paginator.page(page)
    except PageNotAnInteger:
        tweets = paginator.page(1)
    except EmptyPage:
        tweets = paginator.page(paginator.num_pages)

    return render(request,
        'twitter/index.html',
        dict(tweets=tweets, form=form)
    )


@login_required
def reqly(request, tweet_id):
    Tweet = get_object_or_404(Twitter, pk=tweet_id)


@login_required
def twi_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    tweet.delete()
    messages.success(request, '削除しました')
    return redirect('twitter:index')
