from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register

from Tempi.models import ConteggioOrario

from material.admin.sites import site


@register(ConteggioOrario)
class MaterialConteggioOrarioAdmin(MaterialModelAdmin):
    exclude  = ['specialista']
    list_display = ('data_creazione', 'specialista', 'ore',)
    icon_name = 'add_alarm'
    list_filter = ( 'data_creazione',)
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        obj.specialista = request.user
        obj.save()

    def get_queryset(self, request): 
        # For Django < 1.6, override queryset instead of get_queryset
        qs = super(MaterialConteggioOrarioAdmin, self).get_queryset(request)
        if (request.user.is_superuser) :
            return qs
        else:
            return qs.filter(specialista=request.user)
