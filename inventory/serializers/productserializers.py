from rest_framework import serializers
from ..models import Product, Category


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    category_id = serializers.PrimaryKeyRelatedField(
        source="category",
        queryset=Category.objects.all(),
        write_only=True
    )

    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    image = serializers.ImageField(required=False, allow_null=True)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.price = validated_data.get("price", instance.price)
        instance.category = validated_data.get("category", instance.category)
        instance.image = validated_data.get("image", instance.image)
        instance.save()
        return instance