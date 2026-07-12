from django.shortcuts import render
from assets.models import Asset
from maintenance.models import MaintenanceRequest
from bookings.models import ResourceBooking


def reports_dashboard(request):

    context = {
        "total_assets": Asset.objects.count(),
        "available": Asset.objects.filter(status="Available").count(),
        "allocated": Asset.objects.filter(status="Allocated").count(),
        "maintenance": MaintenanceRequest.objects.count(),
        "bookings": ResourceBooking.objects.count(),
    }

    return render(
        request,
        "reports/dashboard.html",
        context,
    )