from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register

from Tempi.models import ConteggioOrario

from material.admin.sites import site
from django.db.models import Sum
import datetime


@register(ConteggioOrario)
class MaterialConteggioOrarioAdmin(MaterialModelAdmin):
    exclude  = ['specialista']
    list_display = ('data_creazione', 'specialista', 'ore',)
    icon_name = 'add_alarm'
    list_filter = ( 'data_creazione',)
    list_per_page = 25
    change_list_template = 'admin/Tempi/Tempi_change_list.html'

    ConteggioOrario.objects.aggregate(Sum('ore'))

    def save_model(self, request, obj, form, change):
        obj.specialista = request.user
        obj.save()

    def get_total(self, request):
        #functions to calculate whatever you want...
        #.filter
        
        data_creazione__gte = request.GET.get('data_creazione__gte')
        data_creazione__lt = request.GET.get('data_creazione__lt')


        if data_creazione__gte != None and data_creazione__lt  != None:
            total  =ConteggioOrario.objects.filter(data_creazione__range =(data_creazione__gte, data_creazione__lt)).aggregate(tot=Sum('ore'))['tot']
        else:
            total  =ConteggioOrario.objects.all().aggregate(tot=Sum('ore'))['tot']


        #total = ConteggioOrario.objects.all().aggregate(tot=Sum('ore'))['tot']
        
        return total

    def changelist_view(self, request, extra_context=None):
        my_context = {
            'total': self.get_total(request),
        }

        return super(MaterialConteggioOrarioAdmin, self).changelist_view(request,
            extra_context=my_context)


    def get_queryset(self, request): 
        # For Django < 1.6, override queryset instead of get_queryset
        qs = super(MaterialConteggioOrarioAdmin, self).get_queryset(request)
        if (request.user.is_superuser) :
            return qs
        else:
            return qs.filter(specialista=request.user)
        
