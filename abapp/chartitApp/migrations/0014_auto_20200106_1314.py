# Generated by Django 2.2.7 on 2020-01-06 12:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chartitApp', '0013_auto_20200106_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creategraph',
            name='inizio',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 12, 14, 15, 145669, tzinfo=utc)),
        ),
    ]
