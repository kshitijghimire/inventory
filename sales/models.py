from django.db import models
from datetime import datetime
from typing import Any

# Create your models here.
class sales(models.Model):
    customer_id = models.IntegerField(default=0)
    product_id= models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    grandTotal= models.IntegerField(default=0)
    date = models.DateField(null=True,default=datetime.now)

