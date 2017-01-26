from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from accounts.forms import SignupForm
from django.contrib.auth.models import User
from twitter.models import Tweet, Favorite


def signup(request):
    form = SignupForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_POST
def signup_save(request):
    form = SignupForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/accounts/login')
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def profile(request, user_id):
    get_user = get_object_or_404(User, pk=user_id)
    tweets = Tweet.objects.filter(user_id_id=user_id).order_by('-id')
    return render(request, 'accounts/profile.html', dict(get_user=get_user, tweets=tweets))

@login_required
def edit(request):
    pass

@login_required
def delete(request):
    return HttpResponse('User削除')
