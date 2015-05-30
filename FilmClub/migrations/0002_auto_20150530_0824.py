# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FilmClub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateTimeField()),
                ('rating', models.IntegerField()),
                ('review', models.CharField(max_length=16383)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='actor1',
            field=models.CharField(default='', max_length=127),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='actor2',
            field=models.CharField(default='', max_length=127),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='actor3',
            field=models.CharField(default='', max_length=127),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='releaseDate',
            field=models.DateField(default=datetime.datetime(2015, 5, 30, 8, 24, 7, 996157, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='runningMinutes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='writer',
            field=models.CharField(default='', max_length=127),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='movie',
            field=models.ForeignKey(to='FilmClub.Movie'),
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(to='FilmClub.Post'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='FilmClub.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
