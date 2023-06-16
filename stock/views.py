from django.shortcuts import render
from .serializers import CategorySerializer, CategoryProductSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import DjangoModelPermissions
from .models import (
    Category,
    Product, 
    Firm, 
    Brand, 
    Purchases, 
    Sales
)


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    filterset_fields = ['name']
    permission_classes = [DjangoModelPermissions]
    
    def get_serializer_class(self):
        if self.request.query_params.get("name"):
            return CategoryProductSerializer
        else:
            return super().get_serializer_class()
        
class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes  = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    
class FirmView(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    permission_classes  = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']