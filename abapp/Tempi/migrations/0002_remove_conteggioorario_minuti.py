# Generated by Django 2.2.7 on 2019-11-18 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tempi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conteggioorario',
            name='minuti',
        ),
    ]
