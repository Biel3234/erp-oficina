from django.urls import path

from .views import WorkOrderCreateList, WorkOrderDetail

urlpatterns = [
    path('', WorkOrderCreateList.as_view()),
    path('<int:pk>/', WorkOrderDetail.as_view()),
]