from rest_framework import serializers
from products_app.models import *

class CategorySeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "name",
            "description"
        ]
class CollectionSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = [
            "name",
            "description"
        ]

class TovarSeriaizer(serializers.ModelSerializer):
    price = serializers.DecimalField(label="Цена", max_digits=10, decimal_places=2)
    class Meta:
        model = Tovar
        fields = [
            "name",
            "description",
            "price",
            "photo",
            "is_exists",
            "category",
            "tovartype",
            "collection",
            "brand"
        ]

class BrendSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Brend
        fields = [
            "name",
            "description",
            "country"
        ]

class TovarTypeSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = TovarType
        fields = [
            "name"
        ]

class NewsSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            "title",
            "text",
            "preview",
            "photo",
            "is_published"
        ]

class ReviewSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "author_name",
            "text",
            "rating",
            "is_approved",
        ]

class PromotionSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = [
            "name",
            "description",
            "discount",
            "start_date",
            "end_date",
            "is_active",
        ]