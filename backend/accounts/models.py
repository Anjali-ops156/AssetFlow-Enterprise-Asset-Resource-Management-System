from django.db import models
from django.contrib.auth.models import User
from organization.models import Department


class Employee(models.Model):

    ROLE_CHOICES = [
        ("Employee", "Employee"),
        ("Department Head", "Department Head"),
        ("Asset Manager", "Asset Manager"),
        ("Admin", "Admin"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default="Employee",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active",
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username