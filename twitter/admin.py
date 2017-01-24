from django.contrib import admin
from twitter.models import Tweet

class TweetAdmin(admin.ModelAdmin):
    list_display=('id', 'user_id_id', 'content', 'created_at', 'reply_tweet_id',)# 一覧に出したい項目
    list_display_links=('id','content',)# 修正リンクでクリックできる項目
admin.site.register(Tweet,TweetAdmin)
