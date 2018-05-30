from django.shortcuts import render
##################MODELOS######################
from apps.UserProfile.models import tb_profile

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