from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from accounts.forms import SignupForm, UserEditForm
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
    login_user = request.user

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=login_user)
        if form.is_valid():
            user = form.save(commit=False)
            user.id = request.user.id
            user.save()
            return redirect('twitter:index')
    else:
        form = UserEditForm(instance=login_user)

    return render(request, 'accounts/edit.html', dict(login_user=login_user, form = form))


@login_required
def delete(request):
    return HttpResponse('User削除')
