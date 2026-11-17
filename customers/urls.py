from .views import (
    CustomerCreateList,
    CustomerDeleteUpdate,
    MotorcycleCreateList,
    MotorcycleDeleteUpdate,
)
from django.urls import path

urlpatterns = [
    path('', CustomerCreateList.as_view()),
    path('<int:pk>', CustomerDeleteUpdate.as_view()),
    path('motorcycles/', MotorcycleCreateList.as_view()),
    path('motorcycles/<int:pk>', MotorcycleDeleteUpdate.as_view()),
]