from django import forms
from django.core.exceptions import ValidationError

from brands.models import Brand


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'slug', 'description', 'status', 'website']

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if len(name) < 2:
            raise ValidationError('Brand Name must be at least 2 characters.')
        return name

    def clean_slug(self):
        slug = self.cleaned_data['slug'].strip().lower()