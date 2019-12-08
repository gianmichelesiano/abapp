from django.contrib.staticfiles.templatetags.staticfiles import static as staticfiles
from django.urls import path, include
from django.utils.translation import ugettext_lazy as _
from django.conf.urls.static import static # new
from django.conf import settings # new
from material.admin.sites import site
from django.conf.urls import url

# optional
###################################################
"""
site.site_header = _('Your site header')
site.site_title = _('Your site title')
site.favicon = staticfiles('path/to/favicon')
site.main_bg_color = 'green'
site.main_hover_color = 'yellow'
site.profile_picture = staticfiles('path/to/image')
site.profile_bg = staticfiles('path/to/image')
site.login_logo = staticfiles('path/to/image')
site.logout_bg = staticfiles('path/to/image')
"""
###################################################

site.site_header = _('Abapp')
site.site_title = _('Abapp')
site.favicon = staticfiles('path/to/favicon')

urlpatterns = [
    path('', include('material.admin.urls')),
    path('admin/', include('material.admin.urls')),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)