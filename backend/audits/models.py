from django.db import models
from django.contrib.auth.models import User
from assets.models import Asset


class AuditCycle(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class AuditRecord(models.Model):

    STATUS = [
        ("Verified", "Verified"),
        ("Missing", "Missing"),
        ("Damaged", "Damaged"),
    ]

    audit = models.ForeignKey(
        AuditCycle,
        on_delete=models.CASCADE
    )

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE
    )

    auditor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS
    )

    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.asset} - {self.status}"