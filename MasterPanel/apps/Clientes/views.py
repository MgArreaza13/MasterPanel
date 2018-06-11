from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
###########MODELOS############
from apps.Clientes.models import tb_cliente

################Formularios##############
from apps.Clientes.forms import ClientRegisterForm

@login_required(login_url = 'Panel:Login' )
def ListadoClientes(request):
	clientes = tb_cliente.objects.all()
	contexto = {
	'clientes':clientes
	}
	return render(request, 'Clientes/listado.html', contexto)
@login_required(login_url = 'Panel:Login' )
def NewClient(request):
	Form = ClientRegisterForm()
	if request.method == 'POST':
		print('METODO ES POST')
		Form = ClientRegisterForm(request.POST, request.FILES  or None)
		if Form.is_valid():
			print('FORMULARIO ES VALIDO')
			Form = Form.save(commit=False)
			Form.user = request.user
			#Form.proveedor = tb_proveedor.objects.get(id = request.POST['proveedor'])
			Form.save()
			return redirect('Clientes:ListadoClientes')
			print('ESTA GUARDADO')
	contexto = {
		'Form' : Form
	}
	return render(request, 'Clientes/NewClient.html', contexto)


def DeleteCliente(request):
	status  = 200
	id_client = request.GET.get('id', None)
	cliente = tb_cliente.objects.get(id = id_client)
	cliente.delete()
	return HttpResponse(status)



def UpdateClient(request , id_client):
	#Form = ClientRegisterForm()
	client = tb_cliente.objects.get(id = id_client)
	if request.method == 'GET':
		Form = ClientRegisterForm(instance = client)
	else:
		Form = ClientRegisterForm(request.POST , request.FILES  ,  instance = client)
		if Form.is_valid():
			cliente = Form.save(commit = False)
			cliente.user = request.user
			cliente.save()
			return redirect('Clientes:ListadoClientes')
		else:
			Form = ClientRegisterForm(request.POST , request.FILES  ,  instance = client)
			print('formulario con errores')
	return render(request, 'Clientes/NewClient.html', {'Form':Form})

def DetallesClient(request, id_client):
	client   = tb_cliente.objects.get(id = id_client)
	contexto = {
		'client':client
	} 
	return render(request, 'Clientes/Detalles.html', contexto)
	