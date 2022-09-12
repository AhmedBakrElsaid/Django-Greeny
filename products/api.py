from rest_framework.response import Response
from .serilizers import ProductSerializer
from .models import Product
from rest_framework.decorators import api_view

# @api_view(['GET'])
# def product_list_api(request):
#     products = Product.objects.all()[:100]
#     data = ProductSerializer(products,many=True).data
#     return Response({"success":True,"Product List":data})



# @api_view(['GET'])
# def product_detail(request,id):
#     product = Product.objects.get(id = id)
#     data = ProductSerializer(product).data
#     return Response({"success":True,'Product':data})

from rest_framework import generics

class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()    