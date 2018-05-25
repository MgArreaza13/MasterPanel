from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from apps.Proyectos.models import tb_proyecto
#from apps.UserProfile.models import tb_profile


class tb_cliente (models.Model):
	user 								=	models.ForeignKey(settings.AUTH_USER_MODEL)
	nameEmpresa							=	models.CharField(default='Sin Datos', null=True, max_length=300)
	RazonSociol							=	models.CharField(default='Sin Datos', null=True, max_length=300)
	Cuit 								=	models.CharField(default='Sin Datos', null=True, max_length=300)
	mailEmpresa							=	models.EmailField(default='sin@datos.com', null=True, max_length=30)
	TelefonoContacto 					=	models.CharField(default='+00000', null=True, max_length=300)
	Nacionalidad						=	models.CharField(default='Sin Datos', null=True, max_length=300)
	namePersonaEncargada				=	models.CharField(default='Sin Datos', null=True, max_length=300)
	montoMensualidad					=	models.CharField(default='0', null=True, max_length=30)		
	FechaCobroMensual					=	models.DateField(blank=False, null=True, default='2018-04-19' )
	urlProject							=	models.URLField(default='http://179.43.123.41:8000/', null=True,max_length=3000)
	Project 	 						= 	models.ForeignKey(tb_proyecto, on_delete=models.CASCADE, null=False, default='Null')
	DateInicioContrato					=	models.DateField(blank=False, null=True, default='2018-04-19' )
	VendedorAsignado					=	models.CharField(default='Sin Datos', null=True, max_length=300)
	dateCreate							=	models.DateField(auto_now=True, blank=False)
	#email 						= 	models.EmailField(default='sin@datos.com', null=True, max_length=30)
	#addressProveedor 			=	models.TextField(default='Sin Datos', null=True)
	#user 						=	models.ForeignKey(settings.AUTH_USER_MODEL)
	#cuit						=	models.IntegerField(default='', null=True)
	#phoneNumberProveedorTwo		=	models.CharField(default='', null=True, max_length=30)
	#personaACargo				=	models.CharField(default='', null=True, max_length=30)
	#paginaWeb 					=	models.URLField(default='', null=True,max_length=3000)
	#urlPhoto					=   models.URLField(default='', null=True,max_length=3000)
	#CollaboratorFavoriteKf		= 	models.ForeignKey(tb_collaborator, on_delete=models.CASCADE, null=False, default='')
	#addressProveedorTwo			= 	models.TextField(default='', null=False)
	#isSendPromotions			=	models.BooleanField()
	#isVip						= 	models.BooleanField()
	#StatusKf					=	models.ForeignKey(tb_status_turn, on_delete=models.CASCADE, null=False, default='')
	#TypeClienteKf				=	models.ForeignKey(tb_type_client, on_delete=models.CASCADE, null=False, default='')
	def __str__(self):
		return self.nameEmpresa
	class Meta:
		managed = True
		db_table = 'Clientes'