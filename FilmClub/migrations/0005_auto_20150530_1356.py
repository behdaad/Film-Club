# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FilmClub', '0004_extendeduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(default='', max_length=127),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='following',
            field=models.ManyToManyField(blank=True, to='FilmClub.ExtendedUser'),
        ),
    ]
