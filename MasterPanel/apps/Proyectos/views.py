from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.Proyectos.models import tb_proyecto
# Create your views here.


@login_required(login_url = 'Panel:Login' )
def ListProyect(request):
	proyectos = tb_proyecto.objects.all()
	contexto = {
	'proyectos':proyectos
	}
	return render(request, 'Proyectos/Listado.html', contexto)