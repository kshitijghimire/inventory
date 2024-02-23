from typing import Any
from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, default='uncategorized')
    category = models.CharField(max_length=50, null = True)
    parent = models.IntegerField(null=True)
    description = models.TextField(null = True)
    added = models.DateField(null = True, default=datetime.now)
    