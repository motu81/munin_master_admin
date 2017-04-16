from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .utils import LoginRequiredMixin
from .models import Group,Host


# Create your views here.
class GroupList(LoginRequiredMixin, ListView):
	model = Group

class GroupCreate(LoginRequiredMixin, CreateView):
	model = Group
	success_url = reverse_lazy('group_list')

class GroupDelete(LoginRequiredMixin, DeleteView):
	model = Group
	success_url = reverse_lazy('group_list')

class HostList(LoginRequiredMixin, ListView):
	model = Host

class HostCreate(LoginRequiredMixin, CreateView):
	model = Host
	success_url = reverse_lazy('host_list')

class HostDelete(LoginRequiredMixin, DeleteView):
	model = Host
	success_url = reverse_lazy('host_list')
