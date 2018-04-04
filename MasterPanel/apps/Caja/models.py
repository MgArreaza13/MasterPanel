from django.db import models
from django.conf import settings
##########################MODELOS############################
from apps.Clientes.models import tb_cliente
from apps.Configuracion.models import tb_tipoIngreso
from apps.Configuracion.models import tb_formasDePago 

# Create your models here.

PAGO_CHOICES = (
    ('Administrador', 'Administrador'),
)
class tb_ingresos (models.Model):
	user			=	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, default='')
	cliente			=  	models.ForeignKey(tb_cliente, on_delete=models.CASCADE, null=False, default='')
	monto 			= 	models.FloatField(default='0', null=True, max_length=30)
	descripcion		= 	models.TextField(default='Sin Descripcion', null=True, max_length=30000)
	formaDePago 	=	models.ForeignKey(tb_formasDePago, on_delete=models.CASCADE, null=False, default='')
	tipoIngreso 	= 	models.ForeignKey(tb_tipoIngreso, on_delete=models.CASCADE, null=False, default='')
	#proyecto 		=	models.ForeignKey(tb_cliente, on_delete=models.CASCADE, null=False, default='')
	#nameUser		=	models.CharField(default='Sin Definir', null=True, max_length=30)
	#lastName		=	models.CharField(default='Sin Definir', null=True, max_length=30)
	#dni 			=	models.CharField(default='A-000000000', null=True, max_length=30)
	#movilTlf		=	models.CharField(default='+000000000', null=True, max_length=30)
	#houseTlf		=	models.CharField(default='+000000000', null=True, max_length=30)
	#mailUser		=	models.EmailField(default='sin@definir.com', null=True, max_length=30)
	#birthdayDate	=	models.DateField(blank=False, null=True, default='1995-04-19' )
	#montoAcumulado	=  	models.FloatField(default='0', null=True, max_length=30)
	#image 			= 	models.ImageField(upload_to='users/avatar/', default='', null=False, )
	#image 			= 	models.ImageField(upload_to='users/avatar/', default='Null', null=True, )
	#tipoUser		=  	models.CharField(max_length=30,null=False,choices=PAGO_CHOICES,default='Administrador',) # Esto se utilizara para saber si es admin, colaborador o client
	dateCreate		=	models.DateField(auto_now=True, blank=False)
	#is_complete		=   models.BooleanField(null=False, blank=True , default=False)
	#nameProfile	=	models.CharField(default='', null=False, max_length=30)
	#StatusKf		= 	models.ForeignKey(tb_status_turn, on_delete=models.CASCADE, null=False, default='')
	def __str__(self):
		return self.user.username
	class Meta:
		managed = True
		db_table = 'ingresos'