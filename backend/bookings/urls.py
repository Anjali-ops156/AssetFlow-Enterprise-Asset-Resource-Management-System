from django.urls import path
from .views import booking_list, create_booking

urlpatterns = [
    path("", booking_list, name="booking_list"),
    path("new/", create_booking, name="create_booking"),
]