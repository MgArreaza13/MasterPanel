from django import forms
#######MODELS###########
from apps.Proyectos.models import tb_proyecto
from django.forms import ModelForm, Media,TextInput, NumberInput,EmailInput,URLInput,PasswordInput,FileInput,Textarea,DateInput,DateTimeInput,Select

from django.forms import extras

class RegisterProject(forms.ModelForm):
	class Meta:
		model = tb_proyecto
		fields = [
		'nameProyecto',
		'dateInicio',
		'developer',
		'logo',
		'dateCreate',
		
		]
		labels = {
			'nameProyecto': 'Nombre del Proyecto',
			'dateInicio': 'Fecha de Inicio',
			'developer': 'Developer',
			'logo': 'Logo',
			'dateCreate': 'Fecha de Creacion',
			
		}
		widgets = {
		'nameProyecto': TextInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			  'placeholder':'Nombre del Proyecto'}),

		'dateInicio': DateInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			  'placeholder':'Fecha de Inicio'}),

		'developer': Select(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			  'placeholder':'Developer'}),

		'logo': FileInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			  'placeholder':'Logo'}),
		
		'dateCreate': DateInput(attrs={'class':'form-control', 
			  'required':'False',
			  'disabled':False,
			  'autocomplete':'off',
			  'placeholder':'Fecha de Creacion'}),

		}

		exclude = ['user', 'dateCreate']