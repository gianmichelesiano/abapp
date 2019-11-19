from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register


from material.admin.sites import site

from programmazione.models import Competenze, Programma


@register(Competenze)
class CompetenzeAdmin(MaterialModelAdmin):
    list_display = ('specialista', 'titolo','data_creazione',)
    icon_name = 'build'

    exclude  = ['specialista']
    list_per_page = 25

    list_filter = ( 'specialista',  'data_creazione',)

    def save_model(self, request, obj, form, change):
        obj.specialista = request.user
        obj.save()


@register(Programma)
class ProgrammaAdmin(MaterialModelAdmin):
    list_display = ('specialista', 'titolo','data_creazione',)
    icon_name = 'list_alt'
    exclude  = ['specialista']
    list_per_page = 25

    list_filter = ( 'specialista',  'data_creazione',)

    def save_model(self, request, obj, form, change):
        obj.specialista = request.user
        obj.save()

