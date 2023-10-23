from django.shortcuts import render
from django.http import HttpResponse
from .models import Entidad,Comunicado

# Create your views here.

def web(request):
    comunicados=Comunicado.objects.all().order_by('-fecha_publicacion')
    entidades=Entidad.objects.all().order_by('-nombre')
   

    data={"comunicados":comunicados,
          "entidades":entidades,
         
    }


    return render(request,'CER2/web.html',data)

