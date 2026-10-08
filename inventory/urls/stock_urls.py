from django.urls import path
from ..views.stock_views import StockListCreateView,StockDetailView

urlpatterns = [
    path('', StockListCreateView.as_view(),name='get_create_stock'),
    path('<int:pk>/', StockDetailView.as_view(), name='detail_stock'),

]
