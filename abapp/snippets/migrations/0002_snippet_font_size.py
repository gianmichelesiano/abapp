# Generated by Django 2.2.7 on 2019-11-18 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='font_size',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]