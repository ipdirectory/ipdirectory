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

def ips(request, unit_pk) :
    template = loader.get_template('list/ips.html')
    current_unit = Unit.objects.get(pk=unit_pk)
    all_ips = current_unit.ip_set.all()
    context = {
        'all_ips': all_ips,
        'unit_pk': unit_pk
    }

    return HttpResponse(template.render(context, request))


def addUnit(request) :
    template = loader.get_template('list/addUnit.html')
    all_ips = Ip.objects.all()
    context = {
        'all_ips': all_ips,
    }

    return HttpResponse(template.render(context, request))


def createUnit(request) :
    template = loader.get_template('list/units.html')

    all_units = Unit.objects.all()
    context = {
        'all_units': all_units,
    }

    if request.POST:
        vLan = request.POST.get('vLan')
        name = request.POST.get('name')
        new_unit = Unit(vLan = vLan, name = name)
        new_unit.save()

    return HttpResponse(template.render(context, request))

