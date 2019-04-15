from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'list'

urlpatterns = [
    path('', views.index, name='index'),
    path('units/', views.units, name='units'),
    #path('ips/', views.ips, name='ips'),
    path('units/add', views.addUnit, name='addUnit'),
    url(r'^units/(?P<unit_pk>[0-9]+)/$', views.ips, name='ips'),
    path('units/createUnit', views.createUnit, name='createUnit'),
    path('test/', views.test, name='test'),

]