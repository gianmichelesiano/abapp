# Generated by Django 2.2.7 on 2019-12-09 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programmazione', '0004_auto_20191209_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='esercizi',
            name='risposta',
        ),
    ]
