from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Products
        fields = "__all__"
