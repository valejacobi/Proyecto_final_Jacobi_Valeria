from django.db import models

class Europa(models.Model):
    destino = models.CharField(max_length=100, null=True, blank=True)
    mes = models.CharField(max_length=30, null=True, blank=True)
    dias = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.destino} - {self.mes}'
    
class America(models.Model):
    destino = models.CharField(max_length=30)
    mes = models.CharField(max_length=30)
    dias = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.destino} - {self.mes} - {self.dias}'

class Africa(models.Model):
    destino = models.CharField(max_length=30)
    mes = models.CharField(max_length=30)
    dias = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.destino} - {self.mes} - {self.dias}'
    
    
class Asia(models.Model):
    destino = models.CharField(max_length=30)
    mes = models.CharField(max_length=30)
    dias = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.destino} - {self.mes} - {self.dias}'
    
class Oceania(models.Model):
    destino = models.CharField(max_length=30)
    mes = models.CharField(max_length=30)
    dias = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.destino} - {self.mes} - {self.dias}'