from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register

from Rapporti.models import AnalisiFunzionale, Relazione

from material.admin.sites import site



@register(Relazione)
class MaterialRelazioneAdmin(MaterialModelAdmin):
    list_display = ('specialista', 'data_creazione',)
    icon_name = 'crop_portrait'

    exclude  = ['specialista']
    list_per_page = 25

    list_filter = ( 'data_creazione', 'specialista')
    search_fields = ('relazione',)

    def save_model(self, request, obj, form, change):
        obj.specialista = request.user
        obj.save()


@register(AnalisiFunzionale)
class MaterialAnalisiFunzionaleAdmin(MaterialModelAdmin):
    list_display = ('specialista', 'data_creazione','comportamento',)
    icon_name = 'warning'

    exclude  = ['specialista']
    list_per_page = 25

    list_filter = ( 'data_creazione', 'specialista')
    search_fields = ('comportamento',)

    def save_model(self, request, obj, form, change):
        obj.specialista = request.user
        obj.save()