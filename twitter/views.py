from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    tweet = "tweetです"
    return render(request,
        'twitter/index.html',
        {'tweet' : tweet}
    )
