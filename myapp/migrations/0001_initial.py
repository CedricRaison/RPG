# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
                ('panoplie', models.CharField(max_length=30)),
                ('vie', models.IntegerField()),
                ('force', models.IntegerField()),
                ('typeOf', models.CharField(max_length=15, choices=[('arme', 'arme'), ('chapeau', 'chapeau'), ('cape', 'cape'), ('botte', 'botte')])),
                ('image', models.ImageField(upload_to=myapp.models.avatar_file_name)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pnj',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
                ('vie', models.IntegerField()),
                ('force', models.IntegerField()),
                ('xp', models.IntegerField()),
                ('avatar', models.ImageField(upload_to=myapp.models.avatar_file_name)),
                ('enigme', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('xp', models.IntegerField()),
                ('item', models.ForeignKey(to='myapp.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('answer', models.CharField(max_length=255)),
                ('enigme', models.ForeignKey(to='myapp.Pnj')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pnj',
            name='quete',
            field=models.ForeignKey(to='myapp.Quete'),
            preserve_default=True,
        ),
    ]
