from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from products.forms import CategoryForm, ProductForm
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
    products = Product.objects.select_related("category", 'brand').all()
    return render(request, "products/product_list.html", {"products" : products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product created successfully")
            return redirect("product_list")

    else:
        form = ProductForm()

    return render(request, "products/product_form.html", {"form" : form, "page_title" : "New Product"})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "products/product_details.html", {"product" : product})

def product_update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully")

    else:
        form = ProductForm(instance=product)

    return render(request, "products/product_form.html", {"form" : form, "page_title" : "Product Update"})


def product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully")
        return redirect("product_list")

    return render(request, "products/product_confirm_delete.html", {"product" : product})