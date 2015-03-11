# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20150129_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnage',
            name='arme',
            field=models.ForeignKey(null=True, related_name='arme', to='myapp.Sac', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personnage',
            name='botte',
            field=models.ForeignKey(null=True, related_name='botte', to='myapp.Sac', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personnage',
            name='cape',
            field=models.ForeignKey(null=True, related_name='cape', to='myapp.Sac', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personnage',
            name='chapeau',
            field=models.ForeignKey(null=True, related_name='chapeau', to='myapp.Sac', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personnage',
            name='inventaire',
            field=models.ManyToManyField(null=True, blank=True, through='myapp.Sac', to='myapp.Item'),
            preserve_default=True,
        ),
    ]
