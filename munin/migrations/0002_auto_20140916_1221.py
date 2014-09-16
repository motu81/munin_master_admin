# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('munin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='group',
            field=models.ForeignKey(blank=True, to='munin.Group', null=True),
        ),
    ]
