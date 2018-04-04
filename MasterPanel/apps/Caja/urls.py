from django.conf.urls import url
from django.contrib import admin
from apps.Caja.views import IngresoList



urlpatterns = [
	#url(r'^$', Configuracion_General, name='Configuracion_General' ),
	url(r'^Ingresos/$', IngresoList, name='IngresoList' ),

  
]