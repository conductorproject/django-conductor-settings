# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conductorsettings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_name', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='serverscheme',
            name='method',
            field=models.CharField(help_text=b'What operation does this scheme support?', max_length=30, choices=[(b'GET', b'GET'), (b'POST', b'POST'), (b'FIND', b'FIND')]),
        ),
        migrations.AlterField(
            model_name='serverscheme',
            name='name',
            field=models.CharField(help_text=b'Name of the scheme', max_length=30, choices=[(b'FILE', b'FILE'), (b'FTP', b'FTP'), (b'SFTP', b'SFTP'), (b'HTTP', b'HTTP')]),
        ),
    ]
