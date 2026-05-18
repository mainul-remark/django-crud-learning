from django.contrib import admin

from products.models import Product, Category


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "status", "created_at")
    search_fields = ("name","slug")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'category', 'price', 'description', 'status')
    search_fields = ('name', 'category__name', 'brand__name')
    list_filter = ('brand', 'category', 'created_at', 'status')