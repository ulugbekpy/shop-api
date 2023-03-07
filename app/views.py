# from django.shortcuts import get_object_or_404
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.generics import RetrieveUpdateDestroyAPIView
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer
from rest_framework.viewsets import ModelViewSet


# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, id):
#     product = get_object_or_404(Product, pk=id)
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response({'message': 'product has been deleted'}, status=status.HTTP_204_NO_CONTENT)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
