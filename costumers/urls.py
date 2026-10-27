from .views import CostumerCreateList
from django.urls import path

urlpatterns = [
    path('', CostumerCreateList.as_view()),
]