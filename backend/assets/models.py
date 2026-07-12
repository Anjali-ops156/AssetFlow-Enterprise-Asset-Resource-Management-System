from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
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

    asset_tag = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )
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

    def save(self, *args, **kwargs):

        if not self.asset_tag:

            last_asset = Asset.objects.order_by("id").last()

            if last_asset:

                try:
                    last_id = int(last_asset.asset_tag.split("-")[1])
                except (IndexError, ValueError):
                    last_id = last_asset.id

                self.asset_tag = f"AF-{last_id + 1:04d}"

            else:
                self.asset_tag = "AF-0001"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.asset_tag} - {self.name}"


class AssetAllocation(models.Model):

    STATUS_CHOICES = [
        ("Allocated", "Allocated"),
        ("Returned", "Returned"),
        ("Transfer Requested", "Transfer Requested"),
    ]

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE
    )

    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    allocated_date = models.DateField(auto_now_add=True)

    expected_return_date = models.DateField(
        null=True,
        blank=True
    )

    returned_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="Allocated"
    )

    condition_notes = models.TextField(blank=True)

    def clean(self):
        if self.status == "Allocated":
            exists = AssetAllocation.objects.filter(
                asset=self.asset,
                status="Allocated"
            ).exclude(id=self.id)

            if exists.exists():
                raise ValidationError(
                    "This asset is already allocated."
                )

    def save(self, *args, **kwargs):
        self.clean()

        if self.status == "Allocated":
            self.asset.status = "Allocated"

        elif self.status == "Returned":
            self.asset.status = "Available"

        self.asset.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.asset.asset_tag} → {self.employee.username}"