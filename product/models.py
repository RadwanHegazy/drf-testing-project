from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    created_by = models.ForeignKey(User, related_name='product_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    test_field = models.CharField(max_length=100)
    body = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.title