from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
	url(r'^$', 'apps.forms.views.login'),
	url(r'^forms/', include('apps.forms.urls', namespace='forms')),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

