# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20150129_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnage',
            name='arme',
            field=models.ForeignKey(to='myapp.Sac', related_name='arme', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personnage',
            name='botte',
            field=models.ForeignKey(to='myapp.Sac', related_name='botte', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personnage',
            name='cape',
            field=models.ForeignKey(to='myapp.Sac', related_name='cape', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personnage',
            name='chapeau',
            field=models.ForeignKey(to='myapp.Sac', related_name='chapeau', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personnage',
            name='inventaire',
            field=models.ManyToManyField(through='myapp.Sac', null=True, to='myapp.Item'),
            preserve_default=True,
        ),
    ]
