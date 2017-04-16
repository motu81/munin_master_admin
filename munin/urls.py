from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from .views import *

urlpatterns = patterns('',
	url(r'^$',				TemplateView.as_view(template_name='munin/main.html'), name='main'),
	url(r'^groups/$',			GroupList.as_view(),      name='group_list'),
	url(r'^groups/add$',			GroupCreate.as_view(),    name='group_create'),
	url(r'^groups/(?P<pk>\d+)/delete$',	GroupDelete.as_view(),    name='group_delete'),
	url(r'^hosts/$',			HostList.as_view(),       name='host_list'),
	url(r'^hosts/add$',			HostCreate.as_view(),     name='host_create'),
	url(r'^hosts/(?P<pk>\d+)/delete$',	HostDelete.as_view(),     name='host_delete'),
)
