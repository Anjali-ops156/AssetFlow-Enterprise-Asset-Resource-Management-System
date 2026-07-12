from django.shortcuts import render
from .models import MaintenanceRequest


def maintenance_list(request):
    requests = MaintenanceRequest.objects.all().order_by("-id")

    return render(
        request,
        "maintenance/maintenance_list.html",
        {"requests": requests},
    )