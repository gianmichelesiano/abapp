# Generated by Django 2.2.7 on 2019-12-08 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rapporti', '0003_auto_20191208_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relazioni',
            name='feedback',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='relazioni',
            name='relazione',
            field=models.TextField(blank=True),
        ),
    ]
