# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conductorsettings', '0007_auto_20150626_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='FindLocationRelativePath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=255)),
                ('location', models.ForeignKey(to='conductorsettings.FindLocation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GetLocationRelativePath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=255)),
                ('location', models.ForeignKey(to='conductorsettings.GetLocation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostLocationRelativePath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=255)),
                ('location', models.ForeignKey(to='conductorsettings.PostLocation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='LocationRelativePath',
        ),
    ]
