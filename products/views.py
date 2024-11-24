from django.http import JsonResponse
from products.models import Product
from products.serializers import ProductSerializer

# View of all products as JSON
def product_list(request):
    all_products = ProductSerializer(Product.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)