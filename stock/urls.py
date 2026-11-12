from django.urls import path
from .views import (PartListCreate, 
                    PartDetail, 
                    CategoryListCreate, 
                    CategoryDetail,
                    MovementListCreate,
                    MovementDetail
                    )

urlpatterns = [
    path('', PartListCreate.as_view()),
    path('<int:pk>', PartDetail.as_view()),
    path('category/', CategoryListCreate.as_view()),
    path('category/<int:pk>', CategoryDetail.as_view()),
    path('movement/', MovementListCreate.as_view()),
    path('movement/<int:pk>', MovementDetail.as_view()),
]