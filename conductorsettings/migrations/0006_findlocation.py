# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conductorsettings', '0005_postlocation'),
    ]

    operations = [
        migrations.CreateModel(
            name='FindLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('media_type', models.CharField(max_length=50)),
                ('authorization', models.CharField(max_length=100, blank=True)),
                ('temporal_rule', models.CharField(default=b'LATEST', max_length=30, choices=[(b'LATEST', b'LATEST'), (b'EARLIEST', b'EARLIEST')])),
                ('parameter_rule', models.CharField(default=b'HIGHEST', max_length=30, choices=[(b'HIGHEST', b'HIGHEST'), (b'LOWEST', b'LOWEST')])),
                ('lock_timeslot_year', models.BooleanField()),
                ('lock_timeslot_month', models.BooleanField()),
                ('lock_timeslot_day', models.BooleanField()),
                ('lock_timeslot_hour', models.BooleanField()),
                ('lock_timeslot_minute', models.BooleanField()),
                ('lock_dekade', models.BooleanField()),
                ('parameter', models.ForeignKey(to='conductorsettings.Parameter')),
                ('resource', models.ForeignKey(related_name='conductorsettings_findlocation_related', to='conductorsettings.Resource')),
                ('server_scheme', models.ForeignKey(related_name='conductorsettings_findlocation_related', to='conductorsettings.ServerScheme')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
