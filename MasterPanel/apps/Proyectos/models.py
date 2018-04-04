from django.db import models
from django.conf import settings
from apps.UserProfile.models import tb_profile


class tb_proyecto (models.Model):
	user 						=	models.ForeignKey(settings.AUTH_USER_MODEL)
	nameProyecto				=	models.CharField(default='Sin Datos', null=True, max_length=30)
	dateInicio					=	models.DateField(blank=False, null=True, default='1995-04-19' )
	developer					=	models.ForeignKey(tb_profile, on_delete=models.CASCADE, null=False, default='Null')
	logo 						= 	models.ImageField(upload_to='proyectos/logo/', default='Null', null=True, )
	#email 						= 	models.EmailField(default='sin@datos.com', null=True, max_length=30)
	#addressProveedor 			=	models.TextField(default='Sin Datos', null=True)
	dateCreate					=	models.DateField(auto_now=True, blank=False)
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
		return self.nameProyecto
	class Meta:
		managed = True
		db_table = 'proyectos'