from django.contrib import admin
from .models import WorkOrder, WorkOrderParts


admin.site.register(WorkOrder)
admin.site.register(WorkOrderParts)