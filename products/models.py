from django.db import models

# Create your models here.

class Product(models.Model):
    Title = models.CharField(max_length=20)
    content = models.TextField(max_length=20)
    price = models.IntegerField()
    
