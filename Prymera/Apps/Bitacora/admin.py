from django.contrib import admin
from .models import *
from django.http import HttpResponse, HttpResponseForbidden
from actions import export_as_csv_action

# Register your models here.
class Admin_Opciones(admin.ModelAdmin):
	list_display=('CATEGORIA','SUB_CATEGORIA','DETALLE_SCATEGORIA','HERRAMIENTA')
    
class Admin_Bitacora(admin.ModelAdmin):
	list_display=('FECHA','FECHA_ENVIO','H_RECEPCION','H_INICIO','H_FIN','ASUNTO','DETALLLE','USUARIO_S','USUARIO_R','USUARIO_A','USUARIO','ESTADO','MEDIO','OPCION','OTRA_AREA')
	actions = [export_as_csv_action("CSV Export", 
		fields=['FECHA','H_RECEPCION','H_INICIO','H_FIN','ASUNTO','DETALLLE','USUARIO_S','USUARIO_R','USUARIO_A','USUARIO','ESTADO','MEDIO','OPCION'])]
	

admin.site.register(Categoria)
admin.site.register(Sub_categoria)
admin.site.register(Detalle_Scategoria)
admin.site.register(Herramienta)
admin.site.register(Opcion,Admin_Opciones)
admin.site.register(Medio)
admin.site.register(Estado)
admin.site.register(Bitacora,Admin_Bitacora)
