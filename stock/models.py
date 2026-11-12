from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Part(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    quantity_in_stock = models.PositiveIntegerField(default=0)
    minimum_stock = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_low(self):
        return self.quantity_in_stock <= self.minimum_stock

    def __str__(self):
        return self.name

class Movement(models.Model):
    MOVEMENTS_TYPES = [
        ('IN', 'Entry'),
        ('OUT', 'Exit'),
    ]

    movement_type = models.CharField(max_length=5, choices=MOVEMENTS_TYPES)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Movement Type: {self.movement_type}, part: {self.part}'