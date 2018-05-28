from django.conf.urls import url
from django.contrib import admin
from apps.Proyectos.views import ListProyect
from apps.Proyectos.views import NewProject
#from apps.Panel.views import Login
#from apps.Panel.views import ComingSoon
#from apps.Panel.views import Logout


urlpatterns = [
	url(r'^$', ListProyect, name='ListProyect' ),
	url(r'^Nuevo/$', NewProject, name='NewProject' ),
	#url(r'^Viene/Pronto$', ComingSoon, name='ComingSoon' ),
	#url(r'^Salir/$', Logout, name='Logout' ),
	#url(r'^calendario/$', calendario, name='calendario' ),
	#url(r'^ingresosegresos/$', ingresosegresos, name='ingresoegresos' ),
	#url(r'^bloqueado/$', loockscreen ,  name='bloqueado' ),
	#url(r'^registro/$', registro ),
  
]