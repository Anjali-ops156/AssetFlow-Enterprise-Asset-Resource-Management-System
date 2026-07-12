from django.shortcuts import render
from django.contrib.auth.models import User

def employee_list(request):
    employees = User.objects.all().order_by("username")

    return render(
        request,
        "organization/employees.html",
        {"employees": employees},
    )