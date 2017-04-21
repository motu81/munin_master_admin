from django.core.management.base import BaseCommand, CommandError
from munin.models import Host
from django.conf import settings

class Command(BaseCommand):
	args = ''
	help = 'writes the munin config'
	
	def handle(self, *args, **options):
		template = """[{group}{host}]\n\taddress {host}\n\tuse_node_name yes\n"""
		with open(settings.MUNIN_CONF_FILE, 'w') as  f:
			for host in Host.objects.all():
				group_prefix = ''
				if host.group:
					group_prefix = host.group.name + ';'
				f.write(template.format(group=group_prefix,host=host.name))
