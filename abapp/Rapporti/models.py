from django.db import models 
from django.utils import timezone
from tinymce.models import HTMLField


class Relazioni(models.Model):
    specialista = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data_creazione = models.DateTimeField(default=timezone.now)
    relazione = models.TextField()
    feedback = models.TextField()
    class Meta:
        verbose_name = 'Relazione'
        verbose_name_plural = 'Relazioni'





class AnalisiFunzionali(models.Model):
    specialista = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data_creazione = models.DateTimeField(default=timezone.now)
    antecedente = models.CharField(max_length=500, blank=True)
    comportamento = models.CharField(max_length=500)
    conseguenza = models.CharField(max_length=500, blank=True)
    reazione = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name = 'Analisi Funzionale'
        verbose_name_plural = 'Analisi Funzionale'

    def __str__(self):
        return self.specialista.username


