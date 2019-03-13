from django.conf.urls import url, include
from . import views
from .views import *

urlpatterns = [
	# social contest prelaunch page
	url(r'^$', views.contest_landing_page, name='contest-landing-page'),
	url(r'^submit/$', views.createUser, name='user-signup'),
	url(r'^share/$', views.thanks_share_us, name='thanks-share-us'),
	url(r'^(?P<ref>[0-9a-zA-Z]+)/$', views.contest_landing_page, name='contest-landing-page'),

]



