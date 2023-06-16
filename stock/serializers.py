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
    
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    
    
    class Meta:
        model = Product
        fields = (
            "name",
            "stock",
            "category",
            "category_id",
            "brand",
            "brand_id",
            "created",
            "updated"
        )
        read_only_fields = ('stock',)
        
    
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
        

class BrandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
            'image'
        )        
        

class FirmSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Firm
        fields = (
            "id",
            "name",
            "phone",
            "address",
            "image",
        )
        

class PurchaseSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()
    
    firm = serializers.StringRelatedField()
    firm_id = serializers.IntegerField()
    
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    
    category = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Purchases
        fields = (
            "id",
            "user",
            "firm",
            "firm_id",
            "brand",
            "brand_id",
            "product",
            "product_id",
            "category",
            "quantity",
            "price",
            "price_total",
            "created",
            "updated",
            
        )
        
        read_only_fields = ('user', "price_total")
        
    def get_category(self,obj):
        return obj.product.category.name
        
        
        

class SalesSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()
    
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    
    category = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Sales
        fields = (
            "id",
            "user",
            "brand",
            "brand_id",
            "product",
            "product_id",
            "category",
            "quantity",
            "price",
            "price_total",
            "created",
            "updated",
            
        )
        
        read_only_fields = ('user', "price_total")
        
    def get_category(self,obj):
        return obj.product.category.name