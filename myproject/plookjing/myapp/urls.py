from django.urls import path
from .views import (
    home, TreeListView, TreeDetailView, PlantTreeView, dashboard,
    TreeListCreateAPIView, TreeRetrieveUpdateAPIView,
)

urlpatterns = [
    # หน้าเว็บหลัก (Frontend)
    path('', home, name='home'),
    path('trees/', TreeListView.as_view(), name='tree_list'),
    path('trees/<int:pk>/', TreeDetailView.as_view(), name='tree_detail'),
    path('trees/<int:pk>/plant/', PlantTreeView.as_view(), name='plant_tree'),
    path('dashboard/', dashboard, name='dashboard'),

    # API สำหรับจัดการข้อมูลต้นไม้
    path('api/trees/', TreeListCreateAPIView.as_view(), name='tree_api_list_create'),
    path('api/trees/<int:pk>/', TreeRetrieveUpdateAPIView.as_view(), name='tree_api_retrieve_update'),
]
