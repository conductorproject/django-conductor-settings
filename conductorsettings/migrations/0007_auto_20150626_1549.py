# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conductorsettings', '0006_findlocation'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationRelativePath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='findlocation',
            name='parameter',
            field=models.ForeignKey(related_name='location', to='conductorsettings.Parameter'),
        ),
    ]
