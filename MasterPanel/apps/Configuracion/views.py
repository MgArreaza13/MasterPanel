from django.shortcuts import render


################MODELOS#################
from apps.Configuracion.models import tb_tipoIngreso
from apps.Configuracion.models import tb_formasDePago


def Configuracion_General(request):
	tipos_de_ingreso =  tb_tipoIngreso.objects.all()
	formas_de_pago = tb_formasDePago.objects.all()
	contexto = {
	'tipos_de_ingreso':tipos_de_ingreso,
	'formas_de_pago':formas_de_pago,
	}
	return render(request, 'Configuracion/Configuracion_General.html', contexto)




