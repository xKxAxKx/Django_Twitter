from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tweet(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_tweet_id = models.IntegerField(null=True, blank=True)
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(default=timezone.now)



class Favorite(models.Model):
    tweet_id = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
