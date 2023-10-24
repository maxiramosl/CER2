from django.shortcuts import render
from django.http import HttpResponse
from .models import Entidad,Comunicado

# Create your views here.

def web(request):
    comunicados=Comunicado.objects.all()
    entidades=Entidad.objects.all().order_by('-nombre')
    seleccionada=request.GET.get("Seleccionada")

    if seleccionada == 'Todos' or seleccionada is None:
        comunicados = Comunicado.objects.filter(visible=True)
    else:
        filtro = Entidad.objects.get(nombre=seleccionada)
        comunicados = Comunicado.objects.filter(entidad=filtro,visible=True)
   
    data={"comunicados":comunicados.order_by('-fecha_publicacion'),
          "entidades":entidades,
          "selecto":seleccionada,
          "comunicadosC":Comunicado.objects.filter(visible=True).order_by('-fecha_publicacion'),
    }


    return render(request,'CER2/web.html',data)

