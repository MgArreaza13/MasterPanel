from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.UserProfile.models import tb_profile
from django.forms import ModelForm, Media,TextInput, NumberInput,EmailInput,URLInput,PasswordInput,FileInput,Textarea,DateInput,DateTimeInput,Select
    
from django.forms import extras



###########FORMULARIO PARA GUARDAR USUARIOS., ESTO ES PROPIO DE DJANG0###################
class UsuarioForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username',]
		exclude = ['email',]#########EXCLUDE EMAIL PORQUE YA LO TENGO EN EL USER PROFILE




########################FORMULARIO PARA GUARDAR EL PERFIL#################################
class ProfileRegisterForm(forms.ModelForm):
	class Meta:
		model = tb_profile
		fields = [
		'nameUser',
		'lastName',
		'dni',
		'movilTlf',
		'mailUser',
		'tipoUser',
		]
		labels = {
		'nameUser':'Primer Nombre',
		'lastName':'Apellidos',
		'dni': 'Documento De Identidad',
		'movilTlf':'Numero Movil de Contacto',
		'mailUser':'Correo Electronico',
		'tipoUser':'Seleccione el tipo de Usuario',
		}
		widgets = {
		'nameUser': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Primer Nombre Del Usuario'}),

		'lastName': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Apellido Del Usuario'}),

		'dni': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Documento De Identidad Del usuario'}),

		'movilTlf': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Ingrese El Numero de Contacto'}),

		'mailUser': EmailInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Ingrese su correo electronico de contacto'}),

		'tipoUser': Select(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Ingrese su imagen de perfil'}),
		#'descriptionProduct': Textarea(attrs={'class':'form-control', 
		#	'required':True ,
		#	 'autofocus':True,
		#	  'autocomplete':'off',
		#	   ,'placeholder':'Direccion Principal Del Nuevo Proveedor',
		#	   'cols': 2, 
		#	   'rows': 6}),
		}
          
		exclude = ['user',  'dateCreate' , 'montoAcumulado', 'montoMensualidad',]
	
		