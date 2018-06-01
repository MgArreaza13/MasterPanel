from django.shortcuts import render
##################MODELOS######################
from apps.UserProfile.models import tb_profile
from apps.Proyectos.models import tb_proyecto


def ListaDeUsuarios(request):
	ListaDeUsuarios = tb_profile.objects.all()
	contexto = {
		'ListaDeUsuarios':ListaDeUsuarios
	}
	return render(request, 'UserProfile/lista.html', contexto)

def ListaDeProgramadores(request):
	ListaDeProgramadores = tb_profile.objects.filter(tipoUser = "Programador")
	contexto = {
		'ListaDeProgramadores':ListaDeProgramadores
	}
	return render(request, 'UserProfile/listadeprogramadores.html', contexto)

def DetallesDeProgramadores(request, id_Programador ):
	DetallesDeProgramadores = tb_profile.objects.filter(tipoUser = "Programador")
	Programador   = tb_profile.objects.get(id = id_Programador)
	proyecto = tb_proyecto.objects.all()
	contexto = {
		'DetallesDeProgramadores':DetallesDeProgramadores,
		'proyecto':proyecto,
		'Programador':Programador

	}
	return render(request, 'UserProfile/DetallesDeProgramadores.html', contexto)