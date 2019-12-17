from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register

from django.contrib import admin
from chartitApp.models import SalesReport, CreateGraph
from material.admin.sites import site
from programmazione.models import Prova

"""
@register(SalesReport)
class MaterialSalesReportAdmin(MaterialModelAdmin):
    list_display = ('month', 'sales', 'product',)
"""

@register(CreateGraph)
class MaterialCreateGraphAdmin(MaterialModelAdmin):
    #list_display = ('inizio', 'fine', 'prova',)
    icon_name = 'insert_chart'
    name = 'Risultati programmazione'
    change_list_template = 'admin/chartitApp/chartitApp_change_list.html'

    
    def changelist_view(self, request, extra_context=None):
        prove = Prova.objects.all()
        my_context = {
            'prove': prove,
        }

        return super(MaterialCreateGraphAdmin, self).changelist_view(request,
            extra_context=my_context)
    
