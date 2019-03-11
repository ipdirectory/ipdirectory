from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'edit'

urlpatterns = [
    #path('', views.index, name='index'),
    #path('units/', views.units, name='units'),
    path('ip/', views.ip, name='ip'),
    path('free/', views.free, name='free'),
    #path('units/add', views.addUnit, name='addUnit'),
    #url(r'^units/(?P<unit_pk>[0-9]+)/$', views.ips, name='ips'),
    #path('units/createUnit', views.createUnit, name='createUnit')

]