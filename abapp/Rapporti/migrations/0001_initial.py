# Generated by Django 2.2.7 on 2019-12-05 08:56

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
            name='Relazioni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_creazione', models.DateTimeField(default=django.utils.timezone.now)),
                ('relazione', models.TextField()),
                ('specialista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Relazione',
                'verbose_name_plural': 'Relazioni',
            },
        ),
        migrations.CreateModel(
            name='AnalisiFunzionali',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_creazione', models.DateTimeField(default=django.utils.timezone.now)),
                ('antecedente', models.CharField(blank=True, max_length=500)),
                ('comportamento', models.CharField(max_length=500)),
                ('conseguenza', models.CharField(blank=True, max_length=500)),
                ('reazione', models.CharField(blank=True, max_length=500)),
                ('specialista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Analisi Funzionale',
                'verbose_name_plural': 'Analisi Funzionale',
            },
        ),
    ]
