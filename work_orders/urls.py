from django.urls import path

from .views import (
    WorkOrderCreateList,
    WorkOrderDetail,
    WorkOrderPartsCreateList,
    WorkOrderPartsDetail,
)

urlpatterns = [
    path('', WorkOrderCreateList.as_view()),
    path('<int:pk>/', WorkOrderDetail.as_view()),
    path('parts/', WorkOrderPartsCreateList.as_view()),
    path('parts/<int:pk>/', WorkOrderPartsDetail.as_view()),
]