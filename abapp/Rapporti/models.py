from django.db import models 
from django.utils import timezone


class Relazione(models.Model):
    specialista = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data_creazione = models.DateTimeField(default=timezone.now)
    relazione = models.TextField()
    class Meta:
        verbose_name = 'Relazione'
        verbose_name_plural = 'Relazioni'



class AnalisiFunzionale(models.Model):
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


class Rinforzo(models.Model):
    specialista = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data_creazione = models.DateTimeField(default=timezone.now)
    rinforzo = models.CharField(max_length=100)
    tipologia = models.CharField(
                    max_length=2,
                    choices=[
                        ('NN', ''),
                        ('CI', 'Cibo'),
                        ('GI', 'Gioco'),
                        ('EL', 'Elettronico'),
                        ('OG', 'Oggetto generico'),
                        ('AL', 'Altro'),
                    ],
                    default='Cibo',
    )   
    class Meta:
        verbose_name = 'Rinforzo'
        verbose_name_plural = 'Rinforzi'

    def __str__(self):
        return self.rinforzo