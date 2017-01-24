from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from accounts.forms import SignupForm


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
def delete(request):
    return HttpResponse('User削除')
