from django.shortcuts import render
from assets.models import Asset
from maintenance.models import MaintenanceRequest

def dashboard(request):
    total_assets = Asset.objects.count()

    available = Asset.objects.filter(
        status="Available"
    ).count()

    allocated = Asset.objects.filter(
        status="Allocated"
    ).count()

    maintenance = Asset.objects.filter(
        status="Under Maintenance"
    ).count()

    active_bookings = 0
    pending_transfers = 0
    upcoming_returns = 0

    recent_requests = MaintenanceRequest.objects.order_by("-id")[:5]

    context = {
        "total_assets": total_assets,
        "available": available,
        "allocated": allocated,
        "maintenance": maintenance,
        "active_bookings": active_bookings,
        "pending_transfers": pending_transfers,
        "upcoming_returns": upcoming_returns,
        "recent_requests": recent_requests,
    }

    return render(request, "dashboard.html", context)