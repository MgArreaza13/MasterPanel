from django.shortcuts import render
from django.shortcuts import redirect
###########MODELOS############
from apps.Caja.models import tb_ingresos
from apps.Caja.models import tb_egreso
################Formularios##############
from apps.Caja.forms import RegisterIngresosForm
from apps.Caja.forms import EgresoRegisterForm

###################vistas##################
def IngresoList(request):
	ingresos = tb_ingresos.objects.all()
	contexto = {
	'ingresos':ingresos,
	}
	return render(request, 'Caja/Ingresos.html', contexto )


def EgresoList(request):
	egresos = tb_egreso.objects.all()
	contexto = {
		'egresos':egresos
	}
	return render(request, 'Caja/Egresos.html', contexto)


	
def NewIngreso(request):
	Form = RegisterIngresosForm()
	if request.method == 'POST':
		Form = RegisterIngresosForm(request.POST, request.FILES  or None)
		if Form.is_valid():
			Form = Form.save(commit=False)
			Form.user = request.user
			Form.save()
			return redirect('Caja:IngresoList')
			
	contexto = {
		'Form': Form
	}
	return render (request, 'Caja/NewIngreso.html', contexto)



def NewEgreso(request):
	Form = EgresoRegisterForm() 
	if request.method == 'POST':
		print('METODO ES POST')
		Form  = EgresoRegisterForm(request.POST, request.FILES  or None)
		if Form.is_valid():
			print('FORMULARIO ES VALIDO')
			Form = Form.save(commit=False)
			Form.user = request.user
			#Form.proveedor = tb_proveedor.objects.get(id = request.POST['proveedor'])
			#Form.tipoDeEgreso = tb_tipoEgreso.objects.get(id= request.POST['tipoDeEgreso'])
			Form.save()
			return redirect('Caja:EgresoList')
			print('ESTA GUARDADO')
		else:
			print('error')
	else:
		pass
	contexto = {
		'Form':Form
	}

	return render(request, 'Caja/newegreso.html', contexto)
	