# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20150129_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('inventaire', models.ForeignKey(to='myapp.Sac')),
                ('item', models.ForeignKey(to='myapp.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
