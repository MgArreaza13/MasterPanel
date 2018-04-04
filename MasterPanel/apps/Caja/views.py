from django.shortcuts import render

###########MODELOS############
from apps.Caja.models import tb_ingresos




###################vistas##################
def IngresoList(request):
	ingresos = tb_ingresos.objects.all()
	contexto = {
	'ingresos':ingresos,
	}
	return render(request, 'Caja/Ingresos.html', contexto )