from django.shortcuts import render

from django.template import loader

from django.http import HttpResponse

from .models import Unit, Ip


def index(request) :
    template = loader.get_template('list/index.html')
    all_ips = Ip.objects.all()
    context = {
        'all_ips' : all_ips,
    }
    return HttpResponse(template.render(context, request))

def units(request) :
    template = loader.get_template('list/units.html')
    all_units = Unit.objects.all()
    context = {
        'all_units': all_units,
    }

    return HttpResponse(template.render(context, request))

def ips(request) :
    template = loader.get_template('list/ips.html')
    all_ips = Ip.objects.all()
    context = {
        'all_ips': all_ips,
    }

    return HttpResponse(template.render(context, request))

