from django.db import models
from django.contrib.auth.models import User
from assets.models import Asset


class MaintenanceRequest(models.Model):

    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("Critical", "Critical"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
        ("Technician Assigned", "Technician Assigned"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved"),
    ]

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE
    )

    requested_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    issue = models.TextField()

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="Medium"
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    technician = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_repairs"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    resolved_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):

        if self.status in [
            "Approved",
            "Technician Assigned",
            "In Progress",
        ]:
            self.asset.status = "Under Maintenance"

        elif self.status == "Resolved":
            self.asset.status = "Available"

        self.asset.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.asset.asset_tag} - {self.status}"