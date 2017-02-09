from django.conf.urls import url
from django.contrib import admin
from posts import views

app_name = 'posts'
urlpatterns = [
	url(r'^$', views.post_list, name='list'),
	url(r'^create/$', views.post_create, name='create_post'),
	url(r'^(?P<id>[\w-]+)/$', views.post_detail, name='detail'),
	url(r'^(?P<id>[\w-]+)/edit/$', views.post_update, name='post_update'),
	url(r'^(?P<id>[\w-]+)/delete/$', views.post_delete),
]