from .views import CostumerCreateList, CostumerDeleteUpdate
from django.urls import path

urlpatterns = [
    path('', CostumerCreateList.as_view()),
    path('<int:pk>', CostumerDeleteUpdate.as_view()),
]