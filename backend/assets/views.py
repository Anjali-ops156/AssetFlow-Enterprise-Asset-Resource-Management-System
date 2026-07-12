from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Asset
from organization.models import AssetCategory
from django.shortcuts import redirect
from .forms import AssetAllocationForm
from notifications.models import Notification
from .forms import AssetForm


@login_required
def asset_list(request):

    assets = Asset.objects.all().order_by("asset_tag")

    search = request.GET.get("search")
    status = request.GET.get("status")
    category = request.GET.get("category")

    if search:
        assets = assets.filter(name__icontains=search)

    if status:
        assets = assets.filter(status=status)

    if category:
        assets = assets.filter(category_id=category)

    categories = AssetCategory.objects.all()

    context = {
        "assets": assets,
        "categories": categories,
    }

    return render(request, "assets/asset_list.html", context)


@login_required
def asset_detail(request, pk):

    asset = get_object_or_404(Asset, pk=pk)

    return render(
        request,
        "assets/asset_detail.html",
        {
            "asset": asset,
        },
    )

@login_required
def add_asset(request):
    if request.method == "POST":
        form = AssetForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("asset_list")
    else:
        form = AssetForm()

    return render(request, "assets/add_asset.html", {"form": form})


@login_required
def allocate_asset(request):

    if request.method == "POST":

        form = AssetAllocationForm(request.POST)

        if form.is_valid():
            allocation = form.save()
            Notification.objects.create(
                user=allocation.employee,
                title="Asset Allocated",
                message=f"You have been allocated {allocation.asset.asset_tag} ({allocation.asset.name})."
                )
            return redirect("asset_list")

    else:

        form = AssetAllocationForm()

    return render(
        request,
        "assets/allocate_asset.html",
        {
            "form": form
        }
    )