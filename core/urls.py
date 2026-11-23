from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Autenticacao (JWT)
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api-auth/', include('rest_framework.urls')),
    # Apps
    path('api/customers/', include('customers.urls')),
    path('api/stock/', include('stock.urls')),
    path('api/services/', include('work_orders.urls')),
]
