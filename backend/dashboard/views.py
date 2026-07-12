from django.shortcuts import render
from assets.models import Asset
from maintenance.models import MaintenanceRequest
from organization.models import Department


def dashboard(request):
    context = {
        "total_assets": Asset.objects.count(),
        "available": Asset.objects.filter(status="Available").count(),
        "allocated": Asset.objects.filter(status="Allocated").count(),
        "maintenance": Asset.objects.filter(status="Under Maintenance").count(),
        "departments": Department.objects.count(),
        "recent_assets": Asset.objects.order_by("-id")[:5],
        "recent_maintenance": MaintenanceRequest.objects.order_by("-id")[:5],
    }

    return render(request, "dashboard.html", context)