from rest_framework import serializers
from products.models import Product

# This class converts data to JSON
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'