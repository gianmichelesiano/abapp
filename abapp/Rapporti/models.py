from django.db import models 
from django.utils import timezone


class Relazione(models.Model):
    specialista = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data_creazione = models.DateTimeField(default=timezone.now)
    relazione = models.TextField()
    class Meta:
        verbose_name = 'Relazione'
        verbose_name_plural = 'Relazioni'


class TableABC(models.Model):
    specialista = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data_creazione = models.DateTimeField(default=timezone.now)
    antecedente = models.CharField(max_length=200, blank=True)
    comportamento = models.CharField(max_length=200)
    conseguenza = models.CharField(max_length=200, blank=True)
    funzione = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Incidente'
        verbose_name_plural = 'Incidenti'

    def __str__(self):
        return self.specialista.username