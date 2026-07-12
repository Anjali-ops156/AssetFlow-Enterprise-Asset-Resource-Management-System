from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
]