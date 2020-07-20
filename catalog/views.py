from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Products
from .serializers import ProductsSerializer
from rest_framework import generics


class ProductView(generics.ListAPIView):
    queryset = Products.objects.filter(is_active=True)
    serializer_class = ProductsSerializer


# class Create(generics.CreateAPIView):
#     serializer_class = ProductsSerializer
