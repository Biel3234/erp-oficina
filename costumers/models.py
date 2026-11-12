from django.db import models

class Costumer(models.Model):

    name = models.CharField(max_length=80)
    phone = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.name

class Motorcycle(models.Model):
    model = models.CharField(max_length=80)
    color = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=7, unique=True)
    owner = models.ForeignKey(Costumer, on_delete=models.PROTECT, null=True)

    def __str__(self):
            return f'{self.model} de {self.owner.name}'