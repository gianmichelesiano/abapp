# Generated by Django 2.2.7 on 2020-01-06 12:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chartitApp', '0012_auto_20200106_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creategraph',
            name='inizio',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 12, 12, 52, 601908, tzinfo=utc)),
        ),
    ]