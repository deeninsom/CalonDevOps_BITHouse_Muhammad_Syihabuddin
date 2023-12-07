from django.db import models
from category.models import Categories
from status.models import Status

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.FloatField()
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name