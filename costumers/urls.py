from .views import CostumerCreateList, CostumerDeleteUpdate, MotorcycleCreateList
from django.urls import path

urlpatterns = [
    path('', CostumerCreateList.as_view()),
    path('<int:pk>', CostumerDeleteUpdate.as_view()),
    path('motorcycles/', MotorcycleCreateList.as_view()),
]