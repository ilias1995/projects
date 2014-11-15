from django.conf.urls import patterns, include, url




urlpatterns = patterns('',
	url(r'^registeration/', 'apps.forms.views.reg', name='registeration'),

	# Examples:
    # url(r'^$', 'zakaz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
)