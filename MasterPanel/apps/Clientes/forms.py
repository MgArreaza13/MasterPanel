from django import forms
from apps.Clientes.models import tb_cliente
from django.forms import ModelForm, Media,TextInput, NumberInput,EmailInput,URLInput,PasswordInput,FileInput,Textarea,DateInput,DateTimeInput,Select
from django.forms import extras

class ClientRegisterForm(forms.ModelForm):
	class Meta:
		model = tb_cliente
		fields = [
		'nameEmpresa',
		'RazonSociol',
		'Cuit',
		'mailEmpresa',
		'TelefonoContacto',
		'Nacionalidad',
		'namePersonaEncargada',
		'montoMensualidad',
		'FechaCobroMensual',
		'urlProject',
		'Project',
		'DateInicioContrato',
		'VendedorAsignado',
		'dateCreate',
		]
		labels = {
			'nameEmpresa': 'Nombre de la Empresa',
			'RazonSociol': 'Razon Social',
			'Cuit': 'Cuit',
			'mailEmpresa': 'Correo Empresarial',
			'TelefonoContacto': 'Telefono de Contacto',
			'Nacionalidad': 'Nacionalidad',
			'namePersonaEncargada': 'Nombre de la Persona Encargada',
			'montoMensualidad': 'Monto Mensualidad',
			'FechaCobroMensual': 'Fecha de Cobro Mensual',
			'urlProject': 'Url Project',
			'Project': 'Project',
			'DateInicioContrato': 'Fecha de Inicio de Contrato',
			'VendedorAsignado': 'Vendedor Asignado',
			'dateCreate': 'Fecha de Creacion',
		}
		widgets = {
		'nameEmpresa': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Nombre de la Empresa'}),

		'RazonSociol': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Razon Social'}),

		'Cuit': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Cuit'}),

		'mailEmpresa': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Correo Empresarial'}),

		'TelefonoContacto': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Telefono de Contacto'}),

		'Nacionalidad': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Nacionalidad'}),

		'namePersonaEncargada': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Nombre de la Persona Encargada'}),

		'montoMensualidad': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Monto Mensualidad'}),

		'FechaCobroMensual': DateTimeInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Fecha de Cobro Mensual'}),

		'urlProject': URLInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Url Project'}),

		'Project': Select(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Project'}),

		'DateInicioContrato': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Fecha de Inicio de Contrato'}),

		'VendedorAsignado': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Vendedor Asignado'}),

		'dateCreate': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Fecha de Creacion'}),

		}
          
		exclude = ['user','dateCreate']