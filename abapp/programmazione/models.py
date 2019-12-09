from django.db import models
from django.utils import timezone

#from programmazione.models import Rinforzi


VOLTE =[
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
    (11, 11),
    (12, 12),
    (13, 13),
    (14, 14),
    (15, 15),
    (16, 16),
    (17, 17),
    (18, 18),
    (19, 19),
    (20, 20),
]

class Rinforzi(models.Model):
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

class Prova(models.Model):
    specialista = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titolo =  models.CharField(max_length=50, blank=True)
    obiettivo =  models.CharField(max_length=50, blank=True)
    procedura =  models.CharField(max_length=50, blank=True)
    attivo  = models.BooleanField(default=False)
    data_creazione = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Prova'
        verbose_name_plural = 'Prove'

    def __str__(self):
        return self.titolo


class Programma(models.Model):
    specialista = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #titolo =  models.CharField(max_length=50, blank=True)
    data_creazione = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Programma'
        verbose_name_plural = 'Programmi'




class Domande(models.Model):
    specialista = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data_creazione = models.DateTimeField(default=timezone.now)
    domanda =  models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Domanda'
        verbose_name_plural = 'Domande'

    def __str__(self):
        return self.domanda

class Esercizi(models.Model):
    programma = models.ForeignKey(Programma, on_delete=models.CASCADE)
    prova = models.ForeignKey(Prova, on_delete=models.CASCADE)
    domanda = models.ManyToManyField(Domande)
    rinforzo = models.ManyToManyField(Rinforzi)

    corretto = models.IntegerField(choices=VOLTE, default=0)
    promt = models.IntegerField(choices=VOLTE, default=0)
    promt_indicativo = models.IntegerField(choices, default=0)
    promt_fisico = models.IntegerField(choices, default=0)
    non_corretto = models.IntegerField(choices, default=0)

    class Meta:
        verbose_name = 'Esercizio'
        verbose_name_plural = 'Esercizi'








