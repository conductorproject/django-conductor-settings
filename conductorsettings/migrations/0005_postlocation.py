# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conductorsettings', '0004_getlocation'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('media_type', models.CharField(max_length=50)),
                ('authorization', models.CharField(max_length=100, blank=True)),
                ('resource', models.ForeignKey(related_name='conductorsettings_postlocation_related', to='conductorsettings.Resource')),
                ('server_scheme', models.ForeignKey(related_name='conductorsettings_postlocation_related', to='conductorsettings.ServerScheme')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
