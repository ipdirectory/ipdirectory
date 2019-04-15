from django.shortcuts import render

from django.template import loader

from django.http import HttpResponse

from list.models import Unit, Ip

from django.http import JsonResponse

def ip(request) :
    
    if request.POST:
        
        ipId = int(request.POST.get('ipId'))
        deviceName = request.POST.get('deviceName')

        selectedIp = Ip.objects.get(id = ipId)
        selectedIp.reserved = True
        selectedIp.device = deviceName
        selectedIp.save()


        print(selectedIp.ipAdress)
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


def free(request) :
    
    if request.POST:
        
        ipId = int(request.POST.get('ipId'))
        deviceName = request.POST.get('deviceName')

        selectedIp = Ip.objects.get(id = ipId)
        selectedIp.reserved = False
        selectedIp.device = 'unreachable'
        selectedIp.save()


        print(selectedIp.ipAdress)
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

def test(request) :
    
    return JsonResponse({'test': 'ok' })