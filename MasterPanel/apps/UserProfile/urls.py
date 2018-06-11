from django.conf.urls import url
from django.contrib import admin
from apps.UserProfile.views import ListaDeUsuarios
from apps.UserProfile.views import ListaDeProgramadores
from apps.UserProfile.views import DetallesDeProgramadores
from apps.UserProfile.views import NewUser
from apps.UserProfile.views import DeleteUser
from apps.UserProfile.views import UpdateUser

urlpatterns = [
	url(r'^$', ListaDeUsuarios , name='ListaDeUsuarios'  ),
	url(r'^Programadores/$', ListaDeProgramadores , name='ListaDeProgramadores'  ),
	url(r'^Nuevo/$', NewUser , name='NewUser'  ),
	url(r'^Nueva/Solicitud/De/Borrar/Usuario$', DeleteUser , name='DeleteUser'  ),
	url(r'^Detalles/(?P<id_Programador>\d+)$', DetallesDeProgramadores , name='DetallesDeProgramadores'  ),
	url(r'^Editar/(?P<id_usuario>\d+)$', UpdateUser, name='UpdateUser'  ),
]