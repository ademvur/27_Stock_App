from django.contrib import admin
from .models import Category, Product, Firm, Brand, Purchases, Sales

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Firm)
admin.site.register(Brand)
admin.site.register(Purchases)
admin.site.register(Sales)