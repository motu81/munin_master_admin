from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import views

urlpatterns = patterns('',
	url(r'^$',                          TemplateView.as_view(template_name='munin/main.html'), name='main'),
	url(r'^groups/$',					views.GroupList.as_view(),      name='group_list'),
	url(r'^groups/add$',				views.GroupCreate.as_view(),    name='group_create'),
	url(r'^groups/(?P<pk>\d+)/delete$',	views.GroupDelete.as_view(),    name='group_delete'),
	url(r'^hosts/$',					views.HostList.as_view(),       name='host_list'),
	url(r'^hosts/add$',					views.HostCreate.as_view(),     name='host_create'),
	url(r'^hosts/(?P<pk>\d+)/delete$',	views.HostDelete.as_view(),     name='host_delete'),
)
