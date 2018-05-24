from django.contrib import admin
from apps.Configuracion.models import tb_tipoIngreso
from apps.Configuracion.models import tb_formasDePago
from apps.Configuracion.models import tb_tipoEgreso
# Register your models here.


admin.site.register(tb_tipoIngreso)
admin.site.register(tb_formasDePago)
admin.site.register(tb_tipoEgreso)
