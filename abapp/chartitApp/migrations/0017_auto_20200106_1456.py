# Generated by Django 2.2.7 on 2020-01-06 13:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chartitApp', '0016_auto_20200106_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creategraph',
            name='inizio',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 13, 56, 21, 807951, tzinfo=utc)),
        ),
    ]