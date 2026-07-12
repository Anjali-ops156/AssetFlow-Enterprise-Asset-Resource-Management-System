from django.shortcuts import render
from assets.models import Asset


def dashboard(request):
    total_assets = Asset.objects.count()
    available = Asset.objects.filter(status="Available").count()
    allocated = Asset.objects.filter(status="Allocated").count()
    maintenance = Asset.objects.filter(status="Under Maintenance").count()

    context = {
        "total_assets": total_assets,
        "available": available,
        "allocated": allocated,
        "maintenance": maintenance,
    }

    return render(request, "dashboard.html", context)