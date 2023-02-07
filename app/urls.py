from django.urls import path
from .views import product_detail, product_list

urlpatterns = [
    path('products/<int:id>/', product_detail, name='product-detail'),
    path('products/list/', product_list, name='product-list'),
]
