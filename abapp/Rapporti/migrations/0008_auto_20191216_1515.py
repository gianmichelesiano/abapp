# Generated by Django 2.2.7 on 2019-12-16 14:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Rapporti', '0007_auto_20191216_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analisifunzionali',
            name='data_creazione',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='relazioni',
            name='data_creazione',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
