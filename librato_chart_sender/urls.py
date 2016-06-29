from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^config/new/$', views.config_new, name='config-new'),
    url(r'^config/edit/(?P<config_id>[0-9]+)/$', views.config_edit, name='config-edit'),
    url(r'^config/delete/(?P<config_id>[0-9]+)/$', views.config_delete, name='config-delete'),
    url(r'^config/send_now/(?P<config_id>[0-9]+)/$', views.send_now, name='send-now'),
    url(r'^login/$', views.login_user),
    url(r'^logout/$', views.logout_user),
]