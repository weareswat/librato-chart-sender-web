from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^config/new.html', views.config_new, name='config-new'),
    url(r'^config/temp.html', views.config_temp, name='config-temp'),
]