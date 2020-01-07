from django.db import models
from django.utils import timezone

class DataFile(models.Model):
    proprietario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nome_documento  = models.CharField(max_length=50, blank=True)
    data_creazione = models.DateTimeField(default=timezone.now)
    data = models.FileField()




    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documenti'

    def save(self, *args, **kwargs):
        super(DataFile, self).save(*args, **kwargs)
        filename = self.data.url


        