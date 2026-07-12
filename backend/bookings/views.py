from django.shortcuts import render, redirect
from .models import ResourceBooking
from .forms import ResourceBookingForm


def booking_list(request):

    bookings = ResourceBooking.objects.all().order_by("-start_time")

    return render(
        request,
        "bookings/booking_list.html",
        {"bookings": bookings},
    )


def create_booking(request):

    if request.method == "POST":

        form = ResourceBookingForm(request.POST)

        if form.is_valid():

            asset = form.cleaned_data["asset"]
            start = form.cleaned_data["start_time"]
            end = form.cleaned_data["end_time"]

            overlap = ResourceBooking.objects.filter(
                asset=asset,
                start_time__lt=end,
                end_time__gt=start,
            ).exists()

            if overlap:

                form.add_error(
                    None,
                    "This asset is already booked for the selected time slot."
                )

            else:

                form.save()

                return redirect("booking_list")

    else:

        form = ResourceBookingForm()

    return render(
        request,
        "bookings/create_booking.html",
        {"form": form},
    )