from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer


@api_view()
def product_detail(self, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer()
    return Response(serializer.data)


@api_view()
def product_list(self):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)
