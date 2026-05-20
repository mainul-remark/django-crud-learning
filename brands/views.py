from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404

from brands.forms import BrandForm
from brands.models import Brand


# Create your views here.

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, "brands/brand_list.html", {"brands" : brands})

def brand_create(request):
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Brand created successfully")
            return redirect("brand_list")
    else:
        form = BrandForm()

    return render(request, "brands/brand_form.html", {"form" : form, "page_title" : "New Brand"})

def brand_update(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)

    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, "Brand updated successfully")
            return redirect("brand_list")

    else:
        form = BrandForm(instance=brand)

    return render(request, "brands/brand_form.html", {"form" : form, "page_title" : "Brand update"})

def brand_delete(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)

    if request.method == "POST":
        try:
            brand.delete()
            messages.success(request, "Brand deleted successfully")
        except ProtectedError:
            messages.error(request, "Brand assigned to product. can\'t be deleted")
            return redirect("brand_list")

    return render(request, "brands/brand_confirm_delete.html", {"brand" : brand})
