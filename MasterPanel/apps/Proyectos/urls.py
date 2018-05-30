from django.conf.urls import url
from django.contrib import admin
from apps.Proyectos.views import ListProyect
from apps.Proyectos.views import NewProject
from apps.Proyectos.views import DetallesProject
from apps.Proyectos.views import DeleteProject
from apps.Proyectos.views import UpdateProject
#from apps.Panel.views import Login
#from apps.Panel.views import ComingSoon
#from apps.Panel.views import Logout


urlpatterns = [
	url(r'^$', ListProyect, name='ListProyect' ),
	url(r'^Nuevo/$', NewProject, name='NewProject' ),
	url(r'^Detalles/(?P<id_proyecto>\d+)$', DetallesProject , name='DetallesProject'  ),
	url(r'^Solicitud/De/Borrar/Proyecto/$', DeleteProject, name='DeleteProject' ),
	url(r'^Editar/(?P<id_proyecto>\d+)$', UpdateProject, name='UpdateProject'  ),
	#url(r'^Viene/Pronto$', ComingSoon, name='ComingSoon' ),
	#url(r'^Salir/$', Logout, name='Logout' ),
	#url(r'^calendario/$', calendario, name='calendario' ),
	#url(r'^ingresosegresos/$', ingresosegresos, name='ingresoegresos' ),
	#url(r'^bloqueado/$', loockscreen ,  name='bloqueado' ),
	#url(r'^registro/$', registro ),
  
]