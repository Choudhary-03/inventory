from django.urls import path
from ..views.sale_views import SaleListView,SaleCreateView,SaleDetailView

urlpatterns = [
    path('', SaleListView.as_view(), name='get_sale'),
    path('create/', SaleCreateView.as_view(), name='create_sale'),
    path('<int:pk>/', SaleDetailView.as_view(),name='detail_sale'),
]
