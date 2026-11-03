from django.db import models

class Motorcycle(models.Model):
    model = models.CharField(max_length=80)
    color = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=7)


class Costumer(models.Model):

    name = models.CharField(max_length=80)
    phone = models.CharField(max_length=13)
    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.PROTECT)