from django.db import models
from organization.models import Department, AssetCategory


class Asset(models.Model):

    STATUS_CHOICES = [
        ("Available", "Available"),
        ("Allocated", "Allocated"),
        ("Reserved", "Reserved"),
        ("Under Maintenance", "Under Maintenance"),
        ("Lost", "Lost"),
        ("Retired", "Retired"),
        ("Disposed", "Disposed"),
    ]

    CONDITION_CHOICES = [
        ("Excellent", "Excellent"),
        ("Good", "Good"),
        ("Fair", "Fair"),
        ("Damaged", "Damaged"),
    ]

    asset_tag = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=150)

    category = models.ForeignKey(
        AssetCategory,
        on_delete=models.CASCADE
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    serial_number = models.CharField(
        max_length=100,
        unique=True
    )

    acquisition_date = models.DateField()

    acquisition_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    location = models.CharField(max_length=100)

    condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOICES,
        default="Good"
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="Available"
    )

    shared_bookable = models.BooleanField(default=False)

    image = models.ImageField(
        upload_to="assets/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.asset_tag} - {self.name}"