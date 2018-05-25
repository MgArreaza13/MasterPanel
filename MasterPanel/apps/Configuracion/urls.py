from django.conf.urls import url
from django.contrib import admin

#####################CONFIGURACION############################
from apps.Configuracion.views import Configuracion_General
###################FORMASS DE PAGO############################
from apps.Configuracion.views import DeleteFormadePago
from apps.Configuracion.views import NewFormadePago
from apps.Configuracion.views import GetFormaDePago
from apps.Configuracion.views import UpdateFormaDePago
from apps.Configuracion.views import FormasdePagoGet






##############################TIPO DE EGRESO###########################################
from apps.Configuracion.views import NuevoTipoDeEgreso
from apps.Configuracion.views import DeleteTipoDeEgreso
from apps.Configuracion.views import GetTipoEgreso
from apps.Configuracion.views import UpdateTipoEgreso



##############################TIPO DE INGRESO###########################################
from apps.Configuracion.views import NuevoTipoDeIngreso
from apps.Configuracion.views import DeleteTipoDeIngreso
from apps.Configuracion.views import GetTipoIngreso
from apps.Configuracion.views import UpdateTipoIngreso


urlpatterns = [

	#######################CONFIGURACION GENERAL ###################################
	url(r'^$', Configuracion_General, name='Configuracion_General' ),
	#########################FORMAS DE PAGO#########################################
	url(r'^Forma/De/Pago/Solicitud/Eliminar/Registro/$', DeleteFormadePago ,  name='DeleteFormadePago' ),
	url(r'^Forma/De/Pago/Solicitud/Nuevo/Registro/$', NewFormadePago ,  name='NewFormadePago' ),
	url(r'^Forma/De/Pago/Solicitud/Get/Registro/$', GetFormaDePago ,  name='GetFormaDePago' ),
	url(r'^Forma/De/Pago/Solicitud/Update/Registro/$', UpdateFormaDePago ,  name='UpdateFormaDePago' ),
  	url(r'^Forma/De/Pago/Solicitud/Get/$', FormasdePagoGet ,  name='FormasdePagoGet' ),
  	
	##############################TIPO DE EGRESO###########################################
	url(r'^Tipo/De/Egreso/Solicitud/Eliminar/Registro/$', DeleteTipoDeEgreso ,  name='DeleteTipoDeEgreso' ),
  	url(r'^Tipo/De/Egreso/Solicitud/Nuevo/Registro/$', NuevoTipoDeEgreso ,  name='NuevoTipoDeEgreso' ),
	url(r'^Tipo/De/Egreso/Get/Registro/$', GetTipoEgreso ,  name='GetTipoEgreso' ),
	url(r'^Tipo/De/Egreso/Update/Registro/$', UpdateTipoEgreso ,  name='UpdateTipoEgreso' ),
	##############################TIPO DE EGRESO###########################################
	url(r'^Tipo/De/Ingreso/Solicitud/Eliminar/Registro/$', DeleteTipoDeIngreso ,  name='DeleteTipoDeIngreso' ),
  	url(r'^Tipo/De/Ingreso/Solicitud/Nuevo/Registro/$', NuevoTipoDeIngreso ,  name='NuevoTipoDeIngreso' ),
	url(r'^Tipo/De/Ingreso/Get/Registro/$', GetTipoIngreso ,  name='GetTipoIngreso' ),
	url(r'^Tipo/De/Ingreso/Update/Registro/$', UpdateTipoIngreso ,  name='UpdateTipoIngreso' ),



]