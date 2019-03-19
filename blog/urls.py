from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.post_list, name='blog'),
    url(r'^new/$', views.make_post,name='new_post'),
]
