
from django.conf.urls import patterns, include, url

from django.contrib import admin




admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^', include('avkpol4.urls', namespace='avkpol4')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),




)
