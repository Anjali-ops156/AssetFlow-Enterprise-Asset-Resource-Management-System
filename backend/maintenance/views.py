from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import MaintenanceRequest
from .forms import MaintenanceRequestForm
from django.shortcuts import get_object_or_404
from notifications.models import Notification


@login_required
def maintenance_list(request):

    requests = MaintenanceRequest.objects.all().order_by("-created_at")

    return render(
        request,
        "maintenance/maintenance_list.html",
        {
            "requests": requests
        }
    )


@login_required
def raise_request(request):

    if request.method == "POST":

        form = MaintenanceRequestForm(request.POST, request.FILES)

        if form.is_valid():

            maintenance = form.save(commit=False)
            maintenance.requested_by = request.user
            maintenance.save()

            return redirect("maintenance_list")

    else:

        form = MaintenanceRequestForm()

    return render(
        request,
        "maintenance/raise_request.html",
        {
            "form": form
        }
    )

@login_required
def approve_request(request, pk):

    maintenance = get_object_or_404(MaintenanceRequest, pk=pk)

    maintenance.status = "Approved"
    maintenance.save()
    Notification.objects.create(
    user=request.user,
    title="Maintenance Request Submitted",
    message=f"Maintenance request raised for {maintenance.asset.asset_tag}."
)

    return redirect("maintenance_list")


@login_required
def resolve_request(request, pk):

    maintenance = get_object_or_404(MaintenanceRequest, pk=pk)

    maintenance.status = "Resolved"
    maintenance.save()
    Notification.objects.create(
    user=maintenance.requested_by,
    title="Maintenance Completed",
    message=f"{maintenance.asset.asset_tag} maintenance has been resolved."
)

    return redirect("maintenance_list")