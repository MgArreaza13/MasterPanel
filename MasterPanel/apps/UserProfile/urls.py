from django.conf.urls import url
from django.contrib import admin
from apps.UserProfile.views import ListaDeUsuarios
from apps.UserProfile.views import ListaDeProgramadores

urlpatterns = [
	url(r'^$', ListaDeUsuarios , name='ListaDeUsuarios'  ),
	url(r'^Programadores/$', ListaDeProgramadores , name='ListaDeProgramadores'  ),

]