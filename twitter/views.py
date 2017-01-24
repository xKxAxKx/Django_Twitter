from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from twitter.models import Tweet, Favorite
from django.contrib.auth.models import User



@login_required
def index(request):
    tweets = Tweet.objects.select_related().all().order_by('-id')
    return render(request,
        'twitter/index.html',
        {'tweets' : tweets}
    )
