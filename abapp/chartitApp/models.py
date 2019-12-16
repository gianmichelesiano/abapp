from django.db import models
from django.utils import timezone

def one_nonths_hence():
    return timezone.now() - timezone.timedelta(days=30)

class SalesReport(models.Model):
    month = models.IntegerField()
    sales = models.FloatField()
    product = models.CharField(max_length= 25)



class CreateGraph(models.Model):
    inizio = models.DateTimeField(default=one_nonths_hence())
    fine = models.DateTimeField(default=timezone.now)
    #product = models.CharField(max_length= 25)
