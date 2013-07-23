from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('ra_web.ra_web.views',
    url(r'^$', 'home'),
    url(r'^api/run-command/$', 'run_command'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
