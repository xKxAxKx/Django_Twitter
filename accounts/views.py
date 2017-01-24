from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def signup(request):
    return HttpResponse('User作成')


@login_required
def delete(request):
    return HttpResponse('User削除')
