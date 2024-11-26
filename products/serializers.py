from rest_framework import serializers
from products.models import Category, Product

# This classes converts data to JSON

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)  # Nested serializer
    
    class Meta:
        model = Product
        fields = '__all__'