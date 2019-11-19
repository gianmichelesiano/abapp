from django.db import models
from django.utils import timezone

class Competenze(models.Model):
    specialista = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titolo =  models.CharField(max_length=50, blank=True)
    obiettivo =  models.CharField(max_length=50, blank=True)
    procedura =  models.CharField(max_length=50, blank=True)
    data_creazione = models.DateTimeField(default=timezone.now)


    class Meta:
        verbose_name = 'Competenza'
        verbose_name_plural = 'Competenze'

    def __str__(self):
        return self.titolo

class Programma(models.Model):
    specialista = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titolo =  models.CharField(max_length=50, blank=True)
    data_creazione = models.DateTimeField(default=timezone.now)
    competenza = models.ManyToManyField(Competenze)

    class Meta:
        verbose_name = 'Programma'
        verbose_name_plural = 'Programmi'

    def __str__(self):
        return self.titolo



