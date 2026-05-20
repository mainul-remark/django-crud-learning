from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from products.forms import CategoryForm
from products.models import Category, Product


# Create your views here.

#category logic functions
def category_list(request):
    categories = Category.objects.all()
    return render(request, "products/category_list.html", {"products": categories})

def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category created successfully")
            return redirect("category_create")

    else:
        form = CategoryForm()

    return render(request, "category/category_form.html", {"form" : form, "page_title" : "New Category"})

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    return render(request, "products/category_detail.html", {"category" : category})

def category_update(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated successfully")
            return redirect("category_list")
    else:
        form = CategoryForm(instance=category)

    return render(request, "category/category_form.html", {"form" : form, "page_title" : "Category Update"})

def category_delete(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    if request.method == "POST":
        category.delete()
        messages.success(request, "Category deleted successfully")
        return redirect("category_list")

    return render(request, "category/category_confirm_delete.html", {"category" : category})

#product logic functions

def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products" : products})