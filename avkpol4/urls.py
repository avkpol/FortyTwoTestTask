from django.conf.urls import patterns, include, url
from django.contrib import admin
from avkpol4 import views

admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^home/', 'avkpol4.views.user_data_view', name='home'),
    url(r'^requests_log/', 'avkpol4.views.request_count', name='request_count'),
    url(r'^save_image/', 'avkpol4.views.user_edit', name='save_image'),
    url(r'^edit/$',views.UserEdit.as_view(), name='user_edit'),

)


