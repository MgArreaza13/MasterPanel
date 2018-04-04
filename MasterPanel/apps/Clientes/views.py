from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.Clientes.models import tb_cliente
# Create your views here.

@login_required(login_url = 'Panel:Login' )
def ListadoClientes(request):
	clientes = tb_cliente.objects.all()
	contexto = {
	'clientes':clientes
	}
	return render(request, 'Clientes/listado.html', contexto)