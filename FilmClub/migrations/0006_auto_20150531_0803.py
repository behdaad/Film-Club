# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FilmClub', '0005_auto_20150530_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=127)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='actor3',
        ),
        migrations.AlterField(
            model_name='movie',
            name='actor1',
            field=models.ForeignKey(to='FilmClub.Person', related_name='actor1'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actor2',
            field=models.ForeignKey(to='FilmClub.Person', related_name='actor2'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(to='FilmClub.Person', related_name='director'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='writer',
            field=models.ForeignKey(to='FilmClub.Person', related_name='writer'),
        ),
    ]
