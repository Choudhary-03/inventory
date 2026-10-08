from rest_framework import serializers
from ..models import Purchase, Product , Supplier

class PurchaseSerializer(serializers.ModelSerializer):

    product_id = serializers.PrimaryKeyRelatedField(
        source="product",
        queryset=Product.objects.all(),
        write_only=True
    )

    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    supplier_id = serializers.PrimaryKeyRelatedField(
        source="supplier",
        queryset=Supplier.objects.all(),
        write_only=True
    )

    supplier_name = serializers.CharField(
        source="supplier.name",
        read_only=True
    )

    class Meta:
        model = Purchase
        fields = [
            "id",
            "product_id",
            "product_name",
            "supplier_id",
            "supplier_name",
            "quantity",
            "purchase_date",
        ]
        
        