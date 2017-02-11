from django.conf.urls import url
from django.contrib.auth.views import login,logout
from accounts import views


urlpatterns = [
    url(r'^login/$', login,
        {'template_name': 'accounts/login.html'},
        name='login'),
    url(r'^logout/$', logout,
        {'template_name': 'accounts/logged_out.html'},
        name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/(?P<user_id>\d+)/$', views.profile, name='profile'),
    url(r'^edit/$', views.edit, name='edit'),
]
