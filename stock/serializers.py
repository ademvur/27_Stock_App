from rest_framework import serializers
from .models import (
    Category,
    Product, 
    Firm, 
    Brand, 
    Purchases, 
    Sales
)


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "product_count",
        )
    
    def get_product_count(self, obj):
        return obj.products.count()
        # return Product.objects.filter(category_id=obj.id).count()
        
        
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"
        
    
class CategoryProductSerializer(serializers.ModelSerializer):

    product_count = serializers.SerializerMethodField()
    products = ProductSerializer(many=True)
    
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "product_count",
            "products",
        )
    
    def get_product_count(self, obj):
        return obj.products.count()
        # return Product.objects.filter(category_id=obj.id).count()