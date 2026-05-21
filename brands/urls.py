# from . import views

from django.urls import path

from . import views

urlpatterns = [
    path("", views.brand_list, name="brand_list"),
    path("create/", views.brand_create, name="brand_create"),
    path("<int:pk>/edit/", views.brand_update, name="brand_update"),
    path("<int:pk>/delete/", views.brand_delete, name="brand_delete"),
]