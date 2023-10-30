from django.db import models

class Europa(models.Model):
    destino = models.CharField(max_length=30)
    mes = models.CharField(max_length=30)
    dias = models.IntegerField()