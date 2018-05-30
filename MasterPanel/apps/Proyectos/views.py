from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
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

def DeleteProject(request):
	status  = 200
	id_project = request.GET.get('id', None)
	proyecto = tb_proyecto.objects.get(id = id_project)
	proyecto.delete()
	return HttpResponse(status)

def UpdateProject(request , id_proyecto):
	#Form = ClientRegisterForm()
	proyecto = tb_proyecto.objects.get(id = id_proyecto)
	if request.method == 'GET':
		Form = RegisterProject(instance = proyecto)
	else:
		Form = RegisterProject(request.POST , request.FILES  ,  instance = proyecto)
		if Form.is_valid():
			proyecto = Form.save(commit = False)
			proyecto.user = request.user
			proyecto.save()
			return redirect('Proyectos:ListProyect')
		else:
			Form = RegisterProject(equest.POST , request.FILES  ,  instance = proyecto)
			print('formulario con errores')
	return render(request, 'Proyectos/NewProject.html', {'Form':Form})


def DetallesProject(request, id_proyecto):
	proyecto =  tb_proyecto.objects.get(id = id_proyecto)
	contexto = {
		'proyecto':proyecto
	}
	return render(request, 'Proyectos/Detalles.html', contexto)