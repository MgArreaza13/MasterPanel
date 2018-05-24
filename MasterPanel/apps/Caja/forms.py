from django import forms
from apps.Caja.models import tb_ingresos
from apps.Caja.models import tb_egreso
from django.forms import ModelForm, Media,TextInput, NumberInput,EmailInput,URLInput,PasswordInput,FileInput,Textarea,DateInput,DateTimeInput,Select
from django.forms import extras

class RegisterIngresosForm(forms.ModelForm):
	class Meta:
		model = tb_ingresos
		fields = [
		'cliente',
		'monto',
		'descripcion',
		'formaDePago',
		'tipoIngreso',
		'dateCreate',
		]
		labels = {
			'cliente': 'Nombre del Cliente',
			'monto': 'Monto',
			'descripcion': 'Descripcion',
			'formaDePago': 'Forma de Pago',
			'tipoIngreso': 'Tipo de Ingreso',
			'dateCreate': 'Fecha de creacion',
		}
		widgets = {
		'cliente': Select(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			  'placeholder':'Nombre del Cliente'}),

		'monto': NumberInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			  'placeholder':'Monto'}),

		'descripcion': Textarea(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			  'placeholder':'descripcion'}),

		'formaDePago': Select(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			  'placeholder':'Forma de Pago'}),
		
		'tipoIngreso': Select(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			  'placeholder':'Tipo de Ingreso'}),

		}

		exclude = ['user', 'dateCreate']


class EgresoRegisterForm(forms.ModelForm):
	class Meta:
		model = tb_egreso
		fields = [
		'monto',
		'descripcion',
		#'proveedor',
		'tipoDeEgreso',
		]
		labels = {
			'monto':'Monto de Egreso',
			'descripcion' :'Descripcion del Egreso',
			'proveedor' :'Proveedor',
			'tipoDeEgreso' :'Tipo de Egreso',	
		}
		widgets = {
		'monto': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Monto de Egreso'}),

		'descripcion': Textarea(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Descripcion del Egreso'}),

		

		'tipoDeEgreso': Select(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			   'placeholder':'Tipo de Egreso'}),

		#'descriptionProduct': Textarea(attrs={'class':'form-control', 
		#	'required':True ,
		#	 'autofocus':True,
		#	  'autocomplete':'off',
		#	   ,'placeholder':'Direccion Principal Del Nuevo Proveedor',
		#	   'cols': 2, 
		#	   'rows': 6}),
		}
          
		exclude = ['user',]