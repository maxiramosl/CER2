from django.db import models
from django.contrib.auth.models import User
#falta: nombre a imprimir, USER y tipo
# Create your models here.
class Entidad(models.Model):
    id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30, default='')
    logo=models.ImageField(default='')

    def __str__(self) -> str:
        return self.nombre
    

class Comunicado(models.Model):
    id=models.BigAutoField(primary_key=True)
    titulo=models.CharField(max_length=30, default='')
    detalle=models.TextField(default='')
    detalle_corto=models.TextField(default='')

    opciones=[ ("S","Suspension de actividades"),
          ("C","Suspension de clase"),
          ("I","Informacion")
    ]
    tipo=models.TextField(max_length=1,choices=opciones, default="")

    entidad= models.ForeignKey(Entidad,on_delete=models.CASCADE)
    visible=models.BooleanField(default=True)
    fecha_publicacion=models.DateTimeField(auto_now=True)
    fecha_ultima_modificacion=models.DateTimeField(auto_now=True)
    publicado_por=models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True)
    modificado_por=models.ForeignKey(User, related_name="modificado_por", on_delete=models.CASCADE, editable=False, null=True)

    def __str__(self) -> str:
        return self.titulo

