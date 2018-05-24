##################MODELOS#################
from apps.Caja.models import tb_ingresos
from apps.Caja.models import tb_egreso
from apps.UserProfile.models import tb_profile
from datetime import date 
from django.db.models import Count, Min, Sum, Avg


def ResumenCaja(request):
	#Total ingresos 
	TotalIngresos = tb_ingresos.objects.all().aggregate(total=Sum('monto'))
	# ingresos mensual 
	totalIngrsos_mensual = tb_ingresos.objects.filter(dateCreate__month = date.today().month).aggregate(total_mensual=Sum('monto'))

	#total Egresos 

	TotalEgresos = tb_egreso.objects.all().aggregate(total=Sum('monto'))
	totalEgresos_mensual = tb_egreso.objects.filter(dateCreate__month = date.today().month).aggregate(total_mensual=Sum('monto'))


	return {'totalIngresos':TotalIngresos, 'totalIngrsos_mensual':totalIngrsos_mensual, 'TotalEgresos':TotalEgresos, 'totalEgresos_mensual':totalEgresos_mensual }



def ResumenMiguelMount(request):
	queryset = tb_profile.objects.get(user__username = 'mgarreaza13')
	return {'miguel_cuenta_socio' : queryset.montoAcumulado}