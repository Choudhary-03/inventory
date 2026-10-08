from django.urls import path
from ..views.purchase_views import PurchaseListCreateView,PurchaseDetailView

urlpatterns = [
    path('', PurchaseListCreateView.as_view(), name='get_create_purchase'),
    path('<int:pk>/', PurchaseDetailView.as_view(), name='detail_purchase'),
]
