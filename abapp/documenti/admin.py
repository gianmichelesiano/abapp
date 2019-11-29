from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register

from documenti.models import DataFile

from material.admin.sites import site


@register(DataFile)
class MaterialDataFileAdmin(MaterialModelAdmin):
    list_display = ('proprietario', 'data_creazione', 'nome_documento', 'data')
    icon_name = 'attach_file'
    #exclude  = ['proprietario']
    list_filter = ( 'data_creazione',)
    #search_fields = ('nome_documento','data')

    list_per_page = 25

    def save_model(self, request, obj, form, change):
        obj.proprietario = request.user
        obj.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions