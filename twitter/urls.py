from django.conf.urls import url
from twitter import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^delete/(?P<tweet_id>\d+)/$', views.twi_delete, name='twi_delete'),
]
