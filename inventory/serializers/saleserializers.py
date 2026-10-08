from rest_framework import serializers
from ..models import Sale, Product

class SaleSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    product_id = serializers.PrimaryKeyRelatedField(
        source="product",
        queryset=Product.objects.all(),
        write_only=True
    )

    class Meta:
        model = Sale
        fields = [
            "id",
            "quantity",
            "sale_date",
            "product_id",
            "product_name"
        ]
