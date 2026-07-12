from django.urls import path
from .views import maintenance_list

urlpatterns = [
    path("", maintenance_list, name="maintenance_list"),
]