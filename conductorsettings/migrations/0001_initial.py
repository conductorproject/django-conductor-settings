# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'A friendly name for this server. It will be used throughout the settings.', max_length=200)),
                ('domain', models.CharField(help_text=b'The domain where this server is accessible.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ServerScheme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('method', models.CharField(max_length=30, choices=[(b'GET', b'GET'), (b'POST', b'POST'), (b'FIND', b'FIND')])),
                ('name', models.CharField(max_length=30, choices=[(b'FILE', b'FILE'), (b'FTP', b'FTP'), (b'SFTP', b'SFTP'), (b'HTTP', b'HTTP')])),
                ('server', models.ForeignKey(related_name='schemes', to='conductorsettings.Server')),
            ],
        ),
        migrations.CreateModel(
            name='ServerSchemeBasePath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=255)),
                ('server_scheme', models.ForeignKey(related_name='base_paths', to='conductorsettings.ServerScheme')),
            ],
        ),
    ]
