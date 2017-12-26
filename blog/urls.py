
from django.conf.urls import url,include

from fugui_blog import  settings

from  blog import views
urlpatterns = [
    url(r'^poll/$', views.poll),
    url(r'^down/$', views.down),
    url(r'^comment/$', views.comment),
    url(r'^backend/$', views.backendIndex),
    url(r'^backend/addarticle/$', views.add_article),
    url(r'^commentTree/(?P<article_id>\d+)/$', views.commentTree),
    url(r'^(?P<username>.*)/(?P<condition>tag|category|date)/(?P<para>.*)', views.homeSite),
    url(r'^(?P<username>.*)/articles/(?P<article_id>\d+)', views.article),

    url(r'^(?P<username>.*)', views.homeSite,name="username"),



]
