from django.conf.urls import patterns, include, url

from django.contrib import admin
from avkpol4 import views


admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^home/', 'avkpol4.views.user_data_view', name='home'),
    url(r'^hide/', 'avkpol4.views.get_from_request', name='hide'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^entry/(?P<pk>\d+)/edit/$',
		views.UserUpdateView.as_view(),
		name='user_edit'),

)
