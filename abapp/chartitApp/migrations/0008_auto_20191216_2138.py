# Generated by Django 2.2.7 on 2019-12-16 20:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chartitApp', '0007_auto_20191216_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creategraph',
            name='prova',
        ),
        migrations.AlterField(
            model_name='creategraph',
            name='inizio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 16, 20, 38, 53, 651824, tzinfo=utc)),
        ),
    ]
