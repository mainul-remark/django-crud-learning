from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

from products.models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description', 'status']

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 3:
            raise ValidationError("Name must be at least 3 characters long.")
        return name

    def clean_slug(self):
        slug = self.cleaned_data["slug"].strip()
        if len(slug) < 3:
            raise ValidationError("Slug must be at least 3 characters long.")
        return slug


class ProductForm(forms.ModelForm):
    document = forms.FileField(
        validators=[FileExtensionValidator(["pdf", "doc", "docx", "png", "jpg", "jpeg"])],
        help_text = "Allowed: pdf, doc, docx, png, jpg, jpeg"
    )

    class Meta:
        model = Product
        fields = ['category', "brand", 'name', 'description', 'price', 'document', "status"]
        widgets = {
            "description":  forms.Textarea(attrs={"rows": 5}),
            "price": forms.NumberInput(attrs={"step" : "0.01"}),
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 3:
            raise ValidationError("Name must be at least 3 characters long.")
        return name

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError("Price must be greater than 0.")
        return price

    def clean_document(self):
        document = self.cleaned_data['document']
        max_size = 3 *1024 * 1024 # in bytes
        if document.size > max_size:
            raise ValidationError("Document size must be less than {} MB.".format(max_size))
        return document

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if name and description and name.lower() in description.lower():
            self.add_error(
                "description",
                "better not use name in description"
            )
        return cleaned_data

