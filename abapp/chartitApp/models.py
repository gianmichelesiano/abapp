from django.db import models

class SalesReport(models.Model):
    month = models.IntegerField()
    sales = models.FloatField()
    product = models.CharField(max_length= 25)
