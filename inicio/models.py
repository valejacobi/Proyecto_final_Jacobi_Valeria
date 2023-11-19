from datetime import date
from django.db import models
from ckeditor.fields import RichTextField



class Europa(models.Model):
    destino = models.CharField(max_length=100, null=True, blank=True)
    mes = models.CharField(max_length=30, null=True, blank=True)
    descripcion = RichTextField(default='')
    dias = models.IntegerField()
    fecha_creacion = models.DateField(default=date.today)
    imagen = models.ImageField(upload_to='destino_img', null=True,blank=True )
    
    def __str__(self):
        return f'{self.id} - {self.destino} - {self.mes}'