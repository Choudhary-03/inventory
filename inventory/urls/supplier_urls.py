from django.urls import path
from ..views.supplier_views import SupplierListCreateView, SupplierDetailView

urlpatterns = [
    path('', SupplierListCreateView.as_view(), name='get_create_supplier'),
    path('<int:pk>/', SupplierDetailView.as_view(), name= ' detail_supplier'),
]
