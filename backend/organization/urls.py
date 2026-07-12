from django.urls import path
from . import views

urlpatterns = [
    path("setup/", views.organization_setup, name="organization_setup"),
]