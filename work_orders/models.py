from costumers.models import Costumer, Motorcycle
from django.db import models
from django.contrib.auth.models import User


class WorkOrder(models.Model):

    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('DIAGNOSIS', 'Under Diagnosis'),
        ('WAITING_APPROVAL', 'Waiting Approval'),
        ('WAITING_FOR_PARTS', 'Waiting for parts'),
        ('IN_PROGRESS', 'In progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Canceled'),
        ('WAITING_PAYMENT', 'Waiting payment'),
        ('FINISHED', 'Finished'),
        ('DELIVERED', 'Delivered to the customer'),
    ]

    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('URGENT', 'Urgent'),
    ]

    costumer = models.ForeignKey(Costumer, on_delete=models.PROTECT)
    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.PROTECT)
    reported_problem = models.TextField(blank=True, default='')
    diagnosis = models.TextField(blank=True, default='')
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    parts_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='OPEN')
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES, default='MEDIUM')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)