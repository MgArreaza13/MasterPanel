from django.shortcuts import render
##################MODELOS######################
from apps.UserProfile.models import tb_profile

def ListaDeUsuarios(request):
	ListaDeUsuarios = tb_profile.objects.all()
	contexto = {
		'ListaDeUsuarios':ListaDeUsuarios
	}
	return render(request, 'UserProfile/lista.html', contexto)