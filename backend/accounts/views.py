from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages


def landing_page(request):
    return render(request, "accounts/landing.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )

        messages.success(request, "Registration successful. Please login.")
        return redirect("login")

    return render(request, "accounts/register.html")


def login_view(request):
    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("landing")


def profile(request):
    return render(request, "accounts/profile.html")