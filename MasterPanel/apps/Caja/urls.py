from django.conf.urls import url
from django.contrib import admin
from apps.Caja.views import IngresoList
from apps.Caja.views import NewIngreso
from apps.Caja.views import EgresoList
from apps.Caja.views import NewEgreso


urlpatterns = [
	#url(r'^$', Configuracion_General, name='Configuracion_General' ),
	url(r'^Ingresos/$', IngresoList, name='IngresoList' ),
	url(r'^Egresos/$', EgresoList, name='EgresoList' ),
	url(r'^Ingresos/Nuevo/$', NewIngreso, name='NewIngreso' ),
	url(r'^Egresos/Nuevo/$', NewEgreso, name='NewEgreso' ),

  
]