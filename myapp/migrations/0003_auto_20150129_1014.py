# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20150129_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnage',
            name='arme',
            field=models.ForeignKey(to='myapp.Sac', related_name='arme', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personnage',
            name='botte',
            field=models.ForeignKey(to='myapp.Sac', related_name='botte', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personnage',
            name='cape',
            field=models.ForeignKey(to='myapp.Sac', related_name='cape', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personnage',
            name='chapeau',
            field=models.ForeignKey(to='myapp.Sac', related_name='chapeau', default=1),
            preserve_default=False,
        ),
    ]
