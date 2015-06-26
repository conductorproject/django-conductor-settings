# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conductorsettings', '0002_auto_20150626_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
                ('value_type', models.CharField(default=b'NUMBER', max_length=50, choices=[(b'NUMBER', b'NUMBER'), (b'STRING', b'STRING')])),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('local_pattern', models.CharField(max_length=255)),
                ('urn', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='parameter',
            name='resource',
            field=models.ForeignKey(related_name='parameters', to='conductorsettings.Resource'),
        ),
    ]
