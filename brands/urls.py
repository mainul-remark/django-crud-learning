# from . import views
from django.views import View
from django.urls import path

urlpatterns = [
    path("", View.brand_list, name="brand_list"),
    path("create/", views.brand_create, name="brand_create"),
    path("<int:pk>/edit/", views.brand_update, name="brand_update"),
    path("<int:pk>/delete/", views.brand_delete, name="brand_delete"),
]