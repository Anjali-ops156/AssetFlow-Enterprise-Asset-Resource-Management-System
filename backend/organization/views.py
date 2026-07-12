from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Department, AssetCategory

def organization_setup(request):
    departments = Department.objects.all()
    categories = AssetCategory.objects.all()
    employees = User.objects.all()

    return render(request, "organization/setup.html", {
        "departments": departments,
        "categories": categories,
        "employees": employees,
    })