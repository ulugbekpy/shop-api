from django.urls import path
from .views import (product_detail, product_list,
                    collection_list, collection_detail)

urlpatterns = [
    path('products/<int:id>/', product_detail, name='product-detail'),
    path('products/list/', product_list, name='product-list'),

    path('collections/<int:id>/', collection_detail),
    path('collections/list/', collection_list),
]
