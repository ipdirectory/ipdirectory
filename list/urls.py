from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('units/', views.units, name='units'),
    path('ips/', views.ips, name='ips')

]