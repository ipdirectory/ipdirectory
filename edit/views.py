from django.shortcuts import render

from django.template import loader

from django.http import HttpResponse

from list.models import Unit, Ip

def ip(request) :
    
    all_units = Unit.objects.all()
    context = {
        'all_units': all_units,
    }

    all_ips = Ip.objects.all()

    if request.POST:
        
        print(request.POST.get('csrfmiddlewaretoken'))
        #vLan = request.POST.get('vLan')
        #name = request.POST.get('name')

        #ip_arr = vLan.split('.')

        #if request.POST.get('check'):
         #   new_unit = Unit(vLan=ip_arr[0] + '.' + ip_arr[1] + '.' + ip_arr[2] + '.' + '0', name=name)
          #  new_unit.save()

           # for ip in range(256):
            #    new_ip = Ip(unit=new_unit, ipAdress=ip_arr[0] + '.' + ip_arr[1] + '.' + ip_arr[2] + '.' + str(ip))
             #   new_ip.save()

    return HttpResponse("Hello")