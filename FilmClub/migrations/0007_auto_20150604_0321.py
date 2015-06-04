# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FilmClub', '0006_auto_20150531_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendeduser',
            name='isMale',
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='gender',
            field=models.CharField(max_length=10, default='male'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.CharField(max_length=127, default=''),
            preserve_default=False,
        ),
    ]
