from django.db import models
from django.conf import settings
# Create your models here.


class tb_tipoIngreso(models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	nameTipoIngreso			=	models.CharField(default='', null=False, max_length=30, unique=True)
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.nameTipoIngreso
	class Meta:
		managed = True
		db_table = 'tipo_de_ingresos'




class tb_formasDePago(models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	nameFormasDePago		=	models.CharField(default='', null=False, max_length=30, unique=True)
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.nameFormasDePago
	class Meta:
		managed = True
		db_table = 'formas_de_pago'	