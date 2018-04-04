##############Modelos#####################
from apps.Clientes.models import tb_cliente 
from apps.Proyectos.models import tb_proyecto
from datetime import date 
from django.db.models import Count, Min, Sum, Avg

def ClientesProcesors(request):
	queryset = tb_cliente.objects.all()
	clientes = len(queryset)
	return {'clientes_total' : clientes }


def ProyectosProcesors(request):
	queryset = tb_proyecto.objects.all()
	proyectos = len(queryset)
	return {'proyectos_total' : proyectos }