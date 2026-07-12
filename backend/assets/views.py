from django.shortcuts import render
from .models import Asset


def asset_list(request):
    assets = Asset.objects.all().order_by("-id")

    context = {
        "assets": assets
    }

    return render(request, "assets/asset_list.html", context)