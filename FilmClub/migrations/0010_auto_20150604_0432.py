# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FilmClub', '0009_extendeduser_has_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extendeduser',
            old_name='displayName',
            new_name='display_name',
        ),
    ]
