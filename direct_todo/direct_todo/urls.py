from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'direct_todo.views.home', name='home'),
    # url(r'^direct_todo/', include('direct_todo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'direct_todo.views.home'),
    url(r'^login/$', 
        'django.contrib.auth.views.login', 
        {
            'template_name': 'index.html'
            }
        ),    
    url(r'^profile/', 'direct_todo.views.profile'),    
    url(r'^admin/', include(admin.site.urls)),    
)

