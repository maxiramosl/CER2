from django.contrib import admin
from .models import Entidad, Comunicado

# Register your models here.
class autentificacion(admin.ModelAdmin):
    list_filter = [("publicado_por",admin.RelatedOnlyFieldListFilter),]
    list_display = ("id","titulo","publicado_por","tipo","fecha_publicacion")
    def save_model(self, request, obj, form, change):
        if not change:
            obj.publicado_por = request.user
        super().save_model(request, obj, form, change)



admin.site.register(Entidad)
admin.site.register(Comunicado,autentificacion)
