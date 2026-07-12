from django.urls import path
from . import views

urlpatterns = [
    path("", views.asset_list, name="asset_list"),
    path("add/", views.add_asset, name="add_asset"),
    path("allocate/", views.allocate_asset, name="allocate_asset"),
    path("<int:pk>/", views.asset_detail, name="asset_detail"),
]