from symtable import Class

from django.core.validators import MinValueValidator
from django.db import models

from brands.models import Brand


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=191, unique=True)
    description = models.TextField(blank=True)
    status = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE,
        related_name='products',
    )
    brand = models.ForeignKey(
        Brand,
        related_name="products",
        on_delete=models.PROTECT
    )
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
    )
    document = models.FileField(upload_to="products/images/")
    status = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name