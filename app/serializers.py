from rest_framework import serializers
from .models import Product, Collection


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'description', 'price']

    def create(self, validated_data):
        product = Product(**validated_data)
        product.other = 1
        product.save()
        return product


class CollectionSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=255)
    # amount = serializers.IntegerField()
    # featured_product = serializers.StringRelatedField()
    class Meta:
        model = Collection
        fields = ['name', 'amount', 'featured_product']

    def create(self, validated_data):
        collection = Collection(**validated_data)
        collection.other = 1
        collection.save()
        return collection
