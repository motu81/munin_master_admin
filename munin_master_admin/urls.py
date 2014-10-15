from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^',         include('munin.urls')),
	url(r'accounts/', include('django.contrib.auth.urls')),
)
