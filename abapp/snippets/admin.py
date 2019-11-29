
from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register

from snippets.models import Snippet

from material.admin.sites import site


@register(Snippet)
class SnippetAdmin(MaterialModelAdmin):
    #exclude = ('title',)
    list_display = ('title', 'body', 'created')
    list_filter = ('created',)
    change_list_template = 'admin/snippets/snippets_change_list.html'
    icon_name = 'attach_file'
