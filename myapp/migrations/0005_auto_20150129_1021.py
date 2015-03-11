# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20150129_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnage',
            name='arme',
            field=models.ForeignKey(blank=True, default=1, to='myapp.Sac', related_name='arme'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personnage',
            name='botte',
            field=models.ForeignKey(blank=True, default=1, to='myapp.Sac', related_name='botte'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personnage',
            name='cape',
            field=models.ForeignKey(blank=True, default=1, to='myapp.Sac', related_name='cape'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personnage',
            name='chapeau',
            field=models.ForeignKey(blank=True, default=1, to='myapp.Sac', related_name='chapeau'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personnage',
            name='inventaire',
            field=models.ManyToManyField(blank=True, to='myapp.Item', through='myapp.Sac'),
            preserve_default=True,
        ),
    ]
