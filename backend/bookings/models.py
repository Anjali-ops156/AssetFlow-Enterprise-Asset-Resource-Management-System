from django.db import models
from django.contrib.auth.models import User
from assets.models import Asset


class ResourceBooking(models.Model):

    STATUS_CHOICES = [
        ("Upcoming", "Upcoming"),
        ("Ongoing", "Ongoing"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE
    )

    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    start_time = models.DateTimeField()

    end_time = models.DateTimeField()

    purpose = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Upcoming"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asset} - {self.employee.username}"