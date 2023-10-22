from django.db import models
#falta: nombre a imprimir, USER y tipo
# Create your models here.
class Entidad(models.Model):
    id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30, default='')
    logo=models.ImageField(default='')

class Comunicado(models.Model):
    id=models.BigAutoField(primary_key=True)
    titulo=models.CharField(max_length=30, default='')
    detalle=models.TextField(default='')
    detalle_corto=models.TextField(default='')

    tipo=[("S","Suspension de actividades"),
          ("C","Suspension de clase"),
          ("I","Informacion"),
    ]

    entidad= models.ForeignKey(Entidad,on_delete=models.CASCADE)
    visible=models.BooleanField(default=True)
    fecha_publicacion=models.DateTimeField(auto_now=True)
    fecha_ultima_modificacion=models.DateTimeField(auto_now=True)
    publicado_por=models.CharField(max_length=30, default='') #CAMBIAR
    modificado_por=models.CharField(max_length=30, default='') #CAMBIAR

