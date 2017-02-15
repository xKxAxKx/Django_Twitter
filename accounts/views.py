from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from accounts.forms import SignupForm, UserEditForm
from django.contrib.auth.models import User
from twitter.models import Tweet, Favorite
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail, EmailMessage
from django_twitter import settings


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        # return HttpResponse(request.POST['email'])
        if form.is_valid():
            form.save()
            #メールの送信(他の処理に分けた方が良いかも???)
            subject = "twitterユーザ作成メール"
            message = "ユーザを作成しました"
            from_email = settings.EMAIL_HOST
            recipient_list = [request.POST['email']]
            send_mail(subject, message, from_email, recipient_list)

            messages.success(request, 'ユーザを作成しました')
            return redirect('/accounts/login')
        else:
            context = {
                'form': form,
            }
            return render(request, 'accounts/signup.html', context)
    else:
        form = SignupForm(request.POST or None)
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
            messages.success(request, '更新しました！')
            return redirect('accounts:profile', user_id=login_user.id)
    else:
        form = UserEditForm(instance=login_user)

    return render(request, 'accounts/edit.html', dict(login_user=login_user, form = form))


@login_required
def delete(request):
    return HttpResponse('User削除')
