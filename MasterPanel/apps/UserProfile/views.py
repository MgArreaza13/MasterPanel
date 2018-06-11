from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
##################MODELOS######################
from apps.UserProfile.models import tb_profile
from apps.Proyectos.models import tb_proyecto
from django.contrib.auth.models import User #Modulo Usuario Django

##################FORMS########################
from apps.UserProfile.forms import UsuarioForm
from apps.UserProfile.forms import ProfileRegisterForm

@login_required(login_url = 'Panel:Login' )
def ListaDeUsuarios(request):
	ListaDeUsuarios = tb_profile.objects.all()
	contexto = {
		'ListaDeUsuarios':ListaDeUsuarios
	}
	return render(request, 'UserProfile/lista.html', contexto)

@login_required(login_url = 'Panel:Login' )
def ListaDeProgramadores(request):
	ListaDeProgramadores = tb_profile.objects.filter(tipoUser = "Programador")
	contexto = {
		'ListaDeProgramadores':ListaDeProgramadores
	}
	return render(request, 'UserProfile/listadeprogramadores.html', contexto)

@login_required(login_url = 'Panel:Login' )
def DetallesDeProgramadores(request, id_Programador ):
	DetallesDeProgramadores = tb_profile.objects.filter(tipoUser = "Programador")
	Programador   = tb_profile.objects.get(id = id_Programador)
	proyecto = tb_proyecto.objects.filter(developer__id = id_Programador)
	contexto = {
		'DetallesDeProgramadores':DetallesDeProgramadores,
		'proyecto':proyecto,
		'Programador':Programador

	}
	return render(request, 'UserProfile/DetallesDeProgramadores.html', contexto)






@login_required(login_url = 'Panel:Login' )
def NewUser(request):
	Form = UsuarioForm()
	Form2 = ProfileRegisterForm()
	fallido = None
	if request.method == 'POST':
		Form  = UsuarioForm(request.POST, request.FILES  or None)
		Form2 = ProfileRegisterForm(request.POST, request.FILES  or None)
		if Form.is_valid() and Form2.is_valid():
			####Guardo el usuario#####
			Form.save()
			usuario = request.POST['username']
			clave 	= request.POST['password1']
			user = auth.authenticate(username=usuario, password=clave)
			if user is not None and user.is_active: #########VEIFICO SI EL USUARIO QUE GUARDE ESTA ACTIVO
				##########Relaciono El Perfil Con El Usuario
				Perfil = Form2.save(commit=False)
				Perfil.user = user
				Perfil.save()
				return redirect('Usuarios:ListaDeUsuarios')
		else:
			Form	= UsuarioForm(request.POST , request.FILES  or None)
			Form2	= ProfileRegisterForm(request.POST, request.FILES  or None)
			fallido = "No pudimos guardar sus datos, intentalo de nuevo luego de verificarlos" 
	contexto = {
	'Form':Form,
	'Form2':Form2,
	'fallido':fallido,
	}
	return render(request, 'UserProfile/NewProfile.html' , contexto)



def DeleteUser(request):
	status = None
	id_usuario = request.GET.get('id', None)
	queryset_2 = tb_profile.objects.get(user__id = id_usuario)
	queryset_2.delete()
	queryset = User.objects.get(id = id_usuario)
	queryset.delete()
	status = 200
	return HttpResponse(status)



@login_required(login_url = 'Panel:Login' )
def UpdateUser(request , id_usuario):
	#Form = ClientRegisterForm()
	usuario = tb_profile.objects.get(id = id_usuario)
	if request.method == 'GET':
		Form = ProfileRegisterForm(instance = usuario)
	else:
		Form = ProfileRegisterForm(request.POST , request.FILES  ,  instance = usuario)
		if Form.is_valid():
			Usuario = Form.save(commit = False)
			Usuario.user = usuario.user
			Usuario.save()
			return redirect('Usuarios:ListaDeUsuarios')
		else:
			Form = ProfileRegisterForm(request.POST , request.FILES  ,  instance = client)
			print('formulario con errores')
	return render(request, 'UserProfile/updateUser.html', {'Form':Form})