from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register

from django.contrib import admin

from material.admin.sites import site

from programmazione.models import Esercizi, Prova, Programma,Domande, Rinforzi

from .forms import EserciziAdminForm

class InLineEsercizi(admin.TabularInline):
    model = Esercizi
    extra = 1

@register(Rinforzi)
class MaterialRinforzoAdmin(MaterialModelAdmin):
    list_display = ('rinforzo', 'tipologia','specialista',)
    exclude  = ['data_creazione', 'specialista']
    icon_name = 'local_pharmacy'

    list_per_page = 25


@register(Programma)
class ProgrammaAdmin(MaterialModelAdmin):
    inlines = [InLineEsercizi]
    list_display = ('specialista' ,'data_creazione',)

    icon_name = 'list_alt'
    exclude  = ['specialista']
    list_per_page = 25

    list_filter = ( 'specialista',  'data_creazione',)

    def save_model(self, request, obj, form, change):
        obj.specialista = request.user
        obj.save()


@register(Prova)
class ProveAdmin(MaterialModelAdmin):
    list_display = ( 'titolo','specialista')
    #list_editable = ('attivo', )
    icon_name = 'build'

    exclude  = ['specialista']

    
    list_per_page = 25

    #list_filter = (  'data_creazione',)

    def save_model(self, request, obj, form, change):
        obj.specialista = request.user
        obj.save()




"""
@register(Esercizi)
class EserciziAdmin(MaterialModelAdmin):
    list_display = ('specialista', 'data_creazione', 'domanda', 'rinforzo', 'risposta')
    icon_name = 'question_answer'

    exclude  = ['specialista']
    list_per_page = 25

    #list_filter = ( 'specialista',  'data_creazione',)

    def save_model(self, request, obj, form, change):
        obj.specialista = request.user
        obj.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

@register(Domande)
class DomandeAdmin(MaterialModelAdmin):
    list_display = ('specialista', 'data_creazione', 'domanda',)
    icon_name = 'help_outline'

    exclude  = ['specialista',  'data_creazione']
    list_per_page = 25

    list_filter = ( 'specialista',  'data_creazione',)

    def save_model(self, request, obj, form, change):
        obj.specialista = request.user
        obj.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
"""






