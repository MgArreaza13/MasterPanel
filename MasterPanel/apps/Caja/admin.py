from django.contrib import admin
from apps.Caja.models import tb_ingresos
from apps.Caja.models import tb_egreso
# Register your models here.

admin.site.register(tb_ingresos)
admin.site.register(tb_egreso)

