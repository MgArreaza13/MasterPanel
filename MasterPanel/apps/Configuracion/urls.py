from django.conf.urls import url
from django.contrib import admin
from apps.Configuracion.views import Configuracion_General



urlpatterns = [
	url(r'^$', Configuracion_General, name='Configuracion_General' ),
	#url(r'^Entrar/$', Login, name='Login' ),

  
]