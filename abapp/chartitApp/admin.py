from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register

from django.contrib import admin
from chartitApp.models import SalesReport, CreateGraph
from material.admin.sites import site


@register(SalesReport)
class MaterialSalesReportAdmin(MaterialModelAdmin):
    list_display = ('month', 'sales', 'product',)


@register(CreateGraph)
class MaterialCreateGraphAdmin(MaterialModelAdmin):
    list_display = ('inizio', 'fine',)

    change_list_template = 'admin/chartitApp/chartitApp_change_list.html'

    """
    def changelist_view(self, request, extra_context=None):
        my_context = {
            'inizio': '2019-11-21',
        }

        return super(MaterialCreateGraphAdmin, self).changelist_view(request,
            extra_context=my_context)
    """
