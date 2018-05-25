from django.conf.urls import url
from django.contrib import admin
from apps.UserProfile.views import ListaDeUsuarios

urlpatterns = [
	url(r'^$', ListaDeUsuarios , name='ListaDeUsuarios'  ),
]