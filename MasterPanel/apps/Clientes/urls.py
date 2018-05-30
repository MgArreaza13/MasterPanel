from django.conf.urls import url
from django.contrib import admin
from apps.Clientes.views import ListadoClientes
from apps.Clientes.views import NewClient
from apps.Clientes.views import DeleteCliente
from apps.Clientes.views import UpdateClient
from apps.Clientes.views import DetallesClient
#from apps.Panel.views import Inicio
#from apps.Panel.views import Login
#from apps.Panel.views import ComingSoon
#from apps.Panel.views import Logout


urlpatterns = [
	url(r'^$', ListadoClientes, name='ListadoClientes' ),
	url(r'^Nuevo/$', NewClient, name='NewClient' ),
	url(r'^Solicitud/De/Borrar/Cliente/$', DeleteCliente, name='DeleteCliente' ),
	url(r'^Editar/(?P<id_client>\d+)$', UpdateClient, name='UpdateClient'  ),
	url(r'^Detalles/(?P<id_client>\d+)$', DetallesClient, name='DetallesClient' ),
	#url(r'^Salir/$', Logout, name='Logout' ),
	#url(r'^calendario/$', calendario, name='calendario' ),
	#url(r'^ingresosegresos/$', ingresosegresos, name='ingresoegresos' ),
	#url(r'^bloqueado/$', loockscreen ,  name='bloqueado' ),
	#url(r'^registro/$', registro ),
  
]