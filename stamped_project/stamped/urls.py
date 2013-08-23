from django.conf.urls import patterns, url
from stamped import views
from stamped_project import settings

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'results/', views.results, name='results'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
)