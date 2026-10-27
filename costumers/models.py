from django.db import models

class Costumer(models.Model):

    name = models.CharField(max_length=80)
    phone = models.CharField(max_length=13)
    motorcycle = models.CharField(max_length=50)