from django.contrib import admin

from brands.models import Brand


# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "description", "website", "status", "created_at", "updated_at")
    search_fields = ("name", "slug")