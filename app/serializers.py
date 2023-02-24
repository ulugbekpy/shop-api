from rest_framework import serializers
from .models import Product, Collection


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'slug', 'description', 'price']

    def create(self, validated_data):
        product = Product(**validated_data)
        product.other = 1
        product.save()
        return product


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'
