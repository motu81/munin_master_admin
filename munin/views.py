from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from models import Group,Host


# Create your views here.
class GroupList(ListView):
	model = Group

class GroupCreate(CreateView):
	model = Group
	success_url = reverse_lazy('group_list')

class GroupDelete(DeleteView):
	model = Group
	success_url = reverse_lazy('group_list')

class HostList(ListView):
	model = Host

class HostCreate(CreateView):
	model = Host
	success_url = reverse_lazy('host_list')

class HostDelete(DeleteView):
	model = Host
	success_url = reverse_lazy('host_list')
