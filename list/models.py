from django.db import models


class Unit(models.Model):
    vLan = models.GenericIPAddressField()
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.vLan + ' : ' + self.name


class Ip(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    ipAdress = models.GenericIPAddressField()
    device = models.CharField(max_length=250, default="unreachable")
    reserved = models.BooleanField(default=False)

    def __str__(self):
        return self.ipAdress+' / ' + self.unit.name