from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

################MODELOS#################
from apps.Configuracion.models import tb_tipoIngreso
from apps.Configuracion.models import tb_formasDePago
from apps.Configuracion.models import tb_tipoEgreso


def Configuracion_General(request):
	tipos_de_ingreso =  tb_tipoIngreso.objects.all()
	formas_de_pago = tb_formasDePago.objects.all()
	tipos_de_egreso = tb_tipoEgreso.objects.all()
	contexto = {
	'tipos_de_ingreso':tipos_de_ingreso,
	'formas_de_pago':formas_de_pago,
	'tipos_de_egreso':tipos_de_egreso
	}
	return render(request, 'Configuracion/Configuracion_General.html', contexto)








################################FORMA DE PAGOS ######################################

def DeleteFormadePago(request):
	status = None
	id_forma_de_pago = request.GET.get('id', None)
	queryset = tb_formasDePago.objects.get(id=id_forma_de_pago)
	queryset.delete()
	status = 200
	return HttpResponse(status)


def NewFormadePago(request):
	status = None
	formadepago = request.GET.get('nombreFormaPago', None)
	queryset = tb_formasDePago.objects.filter(nameFormasDePago = formadepago )
	if (len(queryset) >= 1):
		status = 401
	else:
		formadepago_model = tb_formasDePago()
		formadepago_model.user = request.user
		formadepago_model.nameFormasDePago =  formadepago
		formadepago_model.save()
		status = 200
	return HttpResponse(status)

def GetFormaDePago(request):
	id_forma_de_pago = request.GET.get('id_forma_de_pago', None)
	queryset = tb_formasDePago.objects.get(id= id_forma_de_pago)
	formaDePago = {
		'user':str(queryset.user),
		'formaDePago':queryset.nameFormasDePago,
	}
	return JsonResponse(formaDePago)


def UpdateFormaDePago(request):
	id_forma_de_pago = request.GET.get('id_forma_de_pago', None)
	queryset = tb_formasDePago.objects.get(id= id_forma_de_pago)
	queryset.user = request.user
	queryset.nameFormasDePago = request.GET.get('nombreFormaPago', None)
	queryset.save()
	status = 200 
	return HttpResponse(status)


def FormasdePagoGet(request):
	formas_de_pago = tb_formasDePago.objects.all()
	lista = [{'id': pago.id, 'forma_de_pago': pago.nameFormasDePago} for pago in formas_de_pago]
	data = json.dumps(lista)
	

	return HttpResponse(data)







################################TIPOS DE INGRESOS######################################



def NuevoTipoDeIngreso(request):
	status = None
	tipo_de_ingreso = request.GET.get('TipoDeIngreso', None)
	queryset = tb_tipoIngreso.objects.filter(nameTipoIngreso = tipo_de_ingreso )
	if (len(queryset) >= 1):
		status = 401
	else:
		tipo = tb_tipoIngreso()
		tipo.user = request.user
		tipo.nameTipoIngreso =  tipo_de_ingreso
		tipo.save()
		status = 200
	return HttpResponse(status)


def DeleteTipoDeIngreso(request):
	status = None
	id_tipo_de_ingreso = request.GET.get('id', None)
	queryset = tb_tipoIngreso.objects.get(id=id_tipo_de_ingreso)
	queryset.delete()
	status = 200
	return HttpResponse(status)


def GetTipoIngreso(request):
	id_tipo_de_ingreso = request.GET.get('id_tipo_ingreso', None)
	queryset = tb_tipoIngreso.objects.get(id = id_tipo_de_ingreso)
	tipo_ingreso = {
		'user':str(queryset.user),
		'tipodeIngreso':queryset.nameTipoIngreso,
	}
	return JsonResponse(tipo_ingreso)




def UpdateTipoIngreso(request):
	id_tipo_de_ingreso = request.GET.get('id_tipo_ingreso', None)
	queryset = tb_tipoIngreso.objects.get(id = id_tipo_de_ingreso)
	queryset.user = request.user
	queryset.nameTipoIngreso = request.GET.get('nombre_tipo_ingreso', None)
	queryset.save()
	status = 200 
	return HttpResponse(status)




######################################TIPOS DE EGRESOS#############################################



def NuevoTipoDeEgreso(request):
	status = None
	tipo_de_egreso = request.GET.get('TipoDeEgreso', None)
	queryset = tb_tipoEgreso.objects.filter(tipodeEgreso = tipo_de_egreso )
	if (len(queryset) >= 1):
		status = 401
	else:
		tipo = tb_tipoEgreso()
		tipo.user = request.user
		tipo.tipodeEgreso =  tipo_de_egreso
		tipo.save()
		status = 200
	return HttpResponse(status)


def DeleteTipoDeEgreso(request):
	status = None
	id_tipo_de_egreso = request.GET.get('id', None)
	queryset = tb_tipoEgreso.objects.get(id=id_tipo_de_egreso)
	queryset.delete()
	status = 200
	return HttpResponse(status)


def GetTipoEgreso(request):
	id_tipo_de_egreso = request.GET.get('id_tipo_egreso', None)
	queryset = tb_tipoEgreso.objects.get(id = id_tipo_de_egreso)
	tipo_egreso = {
		'user':str(queryset.user),
		'tipodeEgreso':queryset.tipodeEgreso,
	}
	return JsonResponse(tipo_egreso)




def UpdateTipoEgreso(request):
	id_tipo_de_egreso = request.GET.get('id_tipo_egreso', None)
	queryset = tb_tipoEgreso.objects.get(id = id_tipo_de_egreso)
	queryset.user = request.user
	queryset.tipodeEgreso = request.GET.get('nombre_tipo_egreso', None)
	queryset.save()
	status = 200 
	return HttpResponse(status)
