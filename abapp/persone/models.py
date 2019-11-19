from django.db import models
from django.utils import timezone
from django.conf import settings


class Specialista(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    funzione = models.CharField(
                    max_length=2,
                    choices=[
                        ('TE', 'Terapista'),
                        ('PA', 'Padre'),
                        ('MA', 'Madre'),
                        ('SU', 'Supervisore'),
                        ('DO', 'Dottore'),
                    ],
                    default='TE',
    )
    data_di_inzio = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'Specialista'
        verbose_name_plural = 'Specialisti'

    def __str__(self):
        return self.user.username
