from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register

from persone.models import  Specialista

from material.admin.sites import site
from django.contrib.auth.models import User, Group

#site.unregister(User)
#site.unregister(Group)


@register(Specialista)
class MaterialSpecialistaAdmin(MaterialModelAdmin):
    list_display = ('user', 'funzione',)
    icon_name = 'how_to_reg'
