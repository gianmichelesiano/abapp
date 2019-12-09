from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register

from Rapporti.models import AnalisiFunzionali, Relazioni

from material.admin.sites import site
from .form import RelazioniForm



@register(Relazioni)
class MaterialRelazioneAdmin(MaterialModelAdmin):
    list_display = ('specialista', 'data_creazione','relazione')
    form = RelazioniForm
    icon_name = 'crop_portrait'

    exclude  = ['specialista']
    list_per_page = 25

    list_filter = ( 'data_creazione', 'specialista')
    #search_fields = ('relazione',)

    def save_model(self, request, obj, form, change):
        obj.specialista = request.user
        obj.save()


@register(AnalisiFunzionali)
class MaterialAnalisiFunzionaleAdmin(MaterialModelAdmin):
    list_display = ('specialista', 'data_creazione','comportamento',)
    icon_name = 'warning'

    exclude  = ['specialista']
    list_per_page = 25

    list_filter = ( 'data_creazione', 'specialista')
    #search_fields = ('comportamento',)

    def save_model(self, request, obj, form, change):
        obj.specialista = request.user
        obj.save()



    def save_model(self, request, obj, form, change):
        obj.specialista = request.user
        obj.save()
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions