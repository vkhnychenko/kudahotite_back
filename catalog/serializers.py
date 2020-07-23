from rest_framework import serializers
from .models import Products, Category, ItemsSlider, Subjects, Material, Size, Tags


class ProductsSerializer(serializers.ModelSerializer):
    products = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Products
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Category
        fields = "__all__"


class ItemsSliderSerializer(serializers.ModelSerializer):
    items_slider = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = ItemsSlider
        fields = "__all__"


class SubjectsSerializer(serializers.ModelSerializer):
    subjects = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Subjects
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    material = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Material
        fields = "__all__"


class SizeSerializer(serializers.ModelSerializer):
    size = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Size
        fields = "__all__"


class TagsSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Tags
        fields = "__all__"