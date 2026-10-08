from django.urls import path
from ..views.category_views import CategoryListCreateView,CategoryDetailView

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name= 'list_create_category'),
    path('<int:pk>/', CategoryDetailView.as_view(),name='detail_category'),
]
