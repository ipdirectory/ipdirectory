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
    all_units = Unit.objects.all()
    all_ips = current_unit.ip_set.all()
    context = {
        'all_ips': all_ips,
        'unit_pk': unit_pk,
        'all_units': all_units
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

        ip_arr = vLan.split('.')

        if request.POST.get('check'):
            new_unit = Unit(vLan=ip_arr[0] + '.' + ip_arr[1] + '.' + ip_arr[2] + '.' + '0', name=name)
            new_unit.save()

            for ip in range(256):
                new_ip = Ip(unit=new_unit, ipAdress=ip_arr[0] + '.' + ip_arr[1] + '.' + ip_arr[2] + '.' + str(ip))
                new_ip.save()

    return HttpResponse(template.render(context, request))