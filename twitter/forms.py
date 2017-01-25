from django.forms import ModelForm
from django import forms
from twitter.models import Tweet

class TweetForm(forms.ModelForm):
    """ツイートのフォーム"""
    class Meta:
        model = Tweet
        fields = ('content', 'user_id', )
