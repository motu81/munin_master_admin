from django.db import models

# Create your models here.

default_length=255

class Group(models.Model):
	name=models.CharField(max_length=default_length, unique=True)

	def __str__(self):
		return self.name

class Host(models.Model):
	name=models.CharField(max_length=default_length, unique=True)
	group=models.ForeignKey(Group,null=True,blank=True)

