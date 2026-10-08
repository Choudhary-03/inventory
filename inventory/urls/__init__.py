from django.urls import path, include

urlpatterns = [
    path('product/', include('inventory.urls.product_urls')),
    path('category/', include('inventory.urls.category_urls')),
    path('purchase/', include('inventory.urls.purchase_urls')),
    path('sale/', include('inventory.urls.sale_urls')),
    path('stock/', include('inventory.urls.stock_urls')),
    path('supplier/', include('inventory.urls.supplier_urls')),
]
