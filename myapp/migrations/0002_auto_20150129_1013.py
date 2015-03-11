# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etape',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('etape', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Personnage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nom', models.CharField(unique=True, max_length=30)),
                ('xp', models.IntegerField()),
                ('level', models.IntegerField()),
                ('vie', models.IntegerField()),
                ('force', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('perso', models.ForeignKey(to='myapp.Personnage')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sac',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('item', models.ForeignKey(to='myapp.Item')),
                ('personnage', models.ForeignKey(to='myapp.Personnage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='personnage',
            name='inventaire',
            field=models.ManyToManyField(through='myapp.Sac', to='myapp.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personnage',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='etape',
            name='personnage',
            field=models.ForeignKey(to='myapp.Personnage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='etape',
            name='quete',
            field=models.ForeignKey(to='myapp.Quete'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='pourcXp',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to=myapp.models.item_file_name),
            preserve_default=True,
        ),
    ]
