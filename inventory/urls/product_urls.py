from django.urls import path
from ..views.product_views import ProductListCreateView,ProductDetailView


urlpatterns = [
    path('', ProductListCreateView.as_view(),name= 'list_create_product'),
    path('<int:pk>/',ProductDetailView.as_view(), name= 'detail_product' ),
]
