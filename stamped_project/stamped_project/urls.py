######project level!!
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('stamped.urls')),
    #url(r'results/', include('stamped.urls')),
    # url(r'^stamped_project/', include('stamped_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'stamped/login.html'}, name='login_view'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'template_name': 'stamped/base.html'}, name='logout_view'),
)
