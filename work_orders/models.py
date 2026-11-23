from customers.models import Customer, Motorcycle
from django.contrib.auth.models import User
from django.db import models
from stock.models import Part


class WorkOrder(models.Model):

    STATUS_CHOICES = [
        ('OPEN', 'Aberta'),
        ('DIAGNOSIS', 'Em diagnóstico'),
        ('WAITING_APPROVAL', 'Aguardando aprovação'),
        ('WAITING_FOR_PARTS', 'Aguardando peças'),
        ('IN_PROGRESS', 'Em andamento'),
        ('COMPLETED', 'Concluída'),
        ('CANCELLED', 'Cancelada'),
        ('WAITING_PAYMENT', 'Aguardando pagamento'),
        ('FINISHED', 'Finalizada'),
        ('DELIVERED', 'Entregue ao cliente'),
    ]

    PRIORITY_CHOICES = [
        ('LOW', 'Baixa'),
        ('MEDIUM', 'Média'),
        ('HIGH', 'Alta'),
        ('URGENT', 'Urgente'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
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

class WorkOrderParts(models.Model):
    workorder = models.ForeignKey(WorkOrder, on_delete=models.SET_NULL, null=True)
    part = models.ManyToManyField(Part, through='PartWorkOrder', related_name='work_order_parts')


class PartWorkOrder(models.Model):
    work_order_parts = models.ForeignKey(WorkOrderParts, on_delete=models.CASCADE, related_name='items')
    part = models.ForeignKey(Part, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total(self):
        return self.quantity * self.unit_price