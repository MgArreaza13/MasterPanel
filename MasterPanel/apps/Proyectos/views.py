from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
###########MODELOS############
from apps.Proyectos.models import tb_proyecto
################Formularios##############
from apps.Proyectos.forms import RegisterProject


###################vistas##################
@login_required(login_url = 'Panel:Login' )
def ListProyect(request):
	proyectos = tb_proyecto.objects.all()
	contexto = {
	'proyectos':proyectos
	}
	return render(request, 'Proyectos/Listado.html', contexto)


def NewProject(request):
	Form = RegisterProject()
	if request.method == 'POST':
		Form = RegisterProject(request.POST, request.FILES  or None)
		if Form.is_valid():
			Form = Form.save(commit=False)
			Form.user = request.user
			Form.save()
			return redirect('Proyectos:ListProyect')
			
	contexto = {
		'Form': Form
	}
	return render (request, 'Proyectos/NewProject.html', contexto)

def DetallesProject(request):
	
	return render(request, 'Proyectos/Detalles.html')