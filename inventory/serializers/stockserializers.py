from rest_framework import serializers
from ..models import Stock, Product

class StockSerializer(serializers.ModelSerializer):

    product_id = serializers.PrimaryKeyRelatedField(
        source="product",
        queryset=Product.objects.all(),
        write_only=True
    )

    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    class Meta:
        model = Stock
        fields = [
            "id",
            "product_id",
            "product_name",
            "quantity",
        ]
        