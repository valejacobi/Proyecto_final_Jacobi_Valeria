from django.db import models

class Europa(models.Model):
    destino = models.CharField(max_length=30)
    mes = models.CharField(max_length=30)
    dias = models.IntegerField()
    
class America(models.Model):
    destino = models.CharField(max_length=30)
    mes = models.CharField(max_length=30)
    dias = models.IntegerField()

class Africa(models.Model):
    destino = models.CharField(max_length=30)
    mes = models.CharField(max_length=30)
    dias = models.IntegerField()

class Asia(models.Model):
    destino = models.CharField(max_length=30)
    mes = models.CharField(max_length=30)
    dias = models.IntegerField()
    
class Oceania(models.Model):
    destino = models.CharField(max_length=30)
    mes = models.CharField(max_length=30)
    dias = models.IntegerField()