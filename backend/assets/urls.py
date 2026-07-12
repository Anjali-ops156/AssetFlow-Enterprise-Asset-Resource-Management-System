from django.urls import path
from .views import asset_list, asset_detail

urlpatterns = [
    path("", asset_list, name="asset_list"),
    path("<int:pk>/", asset_detail, name="asset_detail"),
]