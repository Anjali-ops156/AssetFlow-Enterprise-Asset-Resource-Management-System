from django.shortcuts import render
from .models import Asset
from django.shortcuts import get_object_or_404


def asset_list(request):
    assets = Asset.objects.all().order_by("-id")

    search = request.GET.get("search")
    status = request.GET.get("status")

    if search:
        assets = assets.filter(name__icontains=search)

    if status:
        assets = assets.filter(status=status)

    context = {
        "assets": assets
    }

    return render(request, "assets/asset_list.html", context)

def asset_detail(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    return render(request, "assets/asset_detail.html", {"asset": asset})