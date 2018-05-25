from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.Clientes.models import tb_cliente
from django.shortcuts import redirect

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
