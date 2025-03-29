from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField(null = False)
    desc = models.TextField()
    pic = models.ImageField(upload_to="products/", null=False)
    stock = models.PositiveBigIntegerField(default=1)