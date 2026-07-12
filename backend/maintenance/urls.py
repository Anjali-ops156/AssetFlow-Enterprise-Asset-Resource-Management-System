from django.urls import path
from . import views

urlpatterns = [
    path("", views.maintenance_list, name="maintenance_list"),
    path("raise/", views.raise_request, name="raise_request"),
    path("approve/<int:pk>/", views.approve_request, name="approve_request"),
    path("resolve/<int:pk>/", views.resolve_request, name="resolve_request"),
]