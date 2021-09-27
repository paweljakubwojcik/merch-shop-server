from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

# Create your models here.
