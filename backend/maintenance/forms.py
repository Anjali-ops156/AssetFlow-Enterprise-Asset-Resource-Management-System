from django import forms
from .models import MaintenanceRequest


class MaintenanceRequestForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = [
            "asset",
            "issue",
            "priority",
            "photo",
        ]

        widgets = {
            "issue": forms.Textarea(attrs={"rows": 4}),
        }