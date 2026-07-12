from django.shortcuts import render
from .models import ResourceBooking


def booking_list(request):
    bookings = ResourceBooking.objects.all().order_by("-start_time")

    return render(
        request,
        "bookings/booking_list.html",
        {"bookings": bookings},
    )