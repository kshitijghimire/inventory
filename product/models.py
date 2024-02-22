from typing import Any
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, null = True)
    description = models.TextField(null = True)
    picture = models.ImageField(null=True)
    added = models.DateField(null = True)
    updated = models.DateField(null = True)

#Category
#Inventory

