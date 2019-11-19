# Generated by Django 2.2.7 on 2019-11-18 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competenze',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(blank=True, max_length=50)),
                ('obiettivo', models.CharField(blank=True, max_length=50)),
                ('procedura', models.CharField(blank=True, max_length=50)),
                ('data_creazione', models.DateTimeField(default=django.utils.timezone.now)),
                ('specialista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Programma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(blank=True, max_length=50)),
                ('data_creazione', models.DateTimeField(default=django.utils.timezone.now)),
                ('competenza', models.ManyToManyField(to='programmazione.Competenze')),
                ('specialista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
