from django.db import models
from django.contrib.auth.models import User


class UpdateCreate(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True   


class Category(UpdateCreate):
    name = models.CharField(max_length=25)

    
    
    def __str__(self):
        return self.name
    

class Brand(UpdateCreate):
    name = models.CharField(max_length=30, unique=True)
    image = models.TextField()

    
    def __str__(self):
        return self.name
    

class Product(UpdateCreate):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="b_products")
    stock = models.SmallIntegerField(blank=True, default=0)

    
    def __str__(self):
        return self.name
    

class Firm(UpdateCreate):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    image = models.TextField()

    
    def __str__(self):
        return self.name
    
    
class Purchases(UpdateCreate):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, on_delete=models.SET_NULL, null=True, related_name="purchases")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="b_purchases")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="p_purchases")
    quantity = models.SmallIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=8)
    price_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    
    
    def __str__(self):
        return f"{self.user} - {self.product} - {self.quantity}"
    
    
class Sales(UpdateCreate):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="b_sales")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="p_sales")
    quantity = models.SmallIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=8)  
    price_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    
    def __str__(self):
        return f"{self.user} - {self.product} - {self.quantity}"
    
