from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^reading/$', views.ReadingPaper, name="reading"),
    url(r'^listening/$', views.ListeningPaper, name="listening"),
    url(r'^writing/$', views.WritingPaper, name="writing")
    ]
