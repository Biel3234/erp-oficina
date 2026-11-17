from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/customers/', include('customers.urls')),
    path('api/stock/', include('stock.urls')),
    path('api/services/', include('work_orders.urls')),
]
