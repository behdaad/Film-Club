# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FilmClub', '0008_movie_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='has_avatar',
            field=models.BooleanField(default=False),
        ),
    ]
