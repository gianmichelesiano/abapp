# Generated by Django 2.2.7 on 2020-01-06 12:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chartitApp', '0014_auto_20200106_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creategraph',
            name='inizio',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 12, 16, 38, 207633, tzinfo=utc)),
        ),
    ]
