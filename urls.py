import os
from django.conf.urls.defaults import *
from django.conf import settings
from geocoding import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', views.get_basic_map, name='basic-map'),
    url(r'^geolocate/$', views.geolocate, name='geolocate-addresses'),
    
    # Example (not sure what subs for 'foo' here):
    # (r'^olgeopy/', include('olgeopy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(__file__), "media"),
             'show_indexes': True
            }),
    )
    

