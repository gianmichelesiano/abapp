from django.db import models
from django.utils import timezone

class ConteggioOrario(models.Model):
    specialista = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data_creazione = models.DateTimeField(default=timezone.now)
    ore = models.IntegerField(choices=list(zip(range(0, 24), range(0, 24))), default="0", unique=False)
    #minuti = models.IntegerField(choices=list(zip(range(0, 60), range(0, 60))), default="0", unique=False)
    descrizione_attivita = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name = 'Conteggi orario'
        verbose_name_plural = 'Conteggi orari'


    def __str__(self):
        return self.specialista.username +' '+ str(self.data_creazione)
