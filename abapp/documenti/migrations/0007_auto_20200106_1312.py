# Generated by Django 2.2.7 on 2020-01-06 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documenti', '0006_auto_20200106_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datafile',
            name='data_creazione',
            field=models.DateTimeField(blank=True),
        ),
    ]
