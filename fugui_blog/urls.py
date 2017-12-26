from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from fugui_blog import settings

from blog import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'fugui_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login',views.login),
    url(r'^$',views.index),
    url(r'^register/', views.register),
    url(r'^get_validCode_img/', views.get_validCode_img),
    url(r'^index/', views.index),
    url(r'^logout/', views.log_out),
    url(r'^cate/(?P<sitearticlecategory>.*)/$', views.index),
    # 个人站点首页
    url(r'^blog/', include('blog.urls')),
    # media 配置
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^uploadFile/$', views.uploadFile),
]
