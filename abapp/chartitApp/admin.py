from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register

from django.contrib import admin
from chartitApp.models import SalesReport
from material.admin.sites import site


@register(SalesReport)
class MaterialSalesReportAdmin(MaterialModelAdmin):
    list_display = ('month', 'sales', 'product',)

