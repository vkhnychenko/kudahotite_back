from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Products, Category, ItemsSlider, Subjects, Material, Size, Tags
from .serializers import ProductsSerializer, CategorySerializer, ItemsSliderSerializer, SubjectsSerializer,\
    MaterialSerializer, SizeSerializer, TagsSerializer
from rest_framework import generics


class ProductView(generics.ListAPIView):
    queryset = Products.objects.filter(is_active=True)
    serializer_class = ProductsSerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemsSliderView(generics.ListAPIView):
    queryset = ItemsSlider.objects.all()
    serializer_class = ItemsSliderSerializer


class SubjectsView(generics.ListAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer


class MaterialView(generics.ListAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class SizeView(generics.ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class TagsView(generics.ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
