# Generated by Django 2.2.7 on 2019-12-16 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rapporti', '0005_auto_20191208_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relazioni',
            name='feedback',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='relazioni',
            name='relazione',
            field=models.TextField(),
        ),
    ]
