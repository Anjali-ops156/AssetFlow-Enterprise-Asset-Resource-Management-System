from django import forms
from .models import ResourceBooking


class ResourceBookingForm(forms.ModelForm):

    class Meta:
        model = ResourceBooking

        fields = [
            "asset",
            "employee",
            "start_time",
            "end_time",
            "purpose",
        ]

        widgets = {
            "start_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "end_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }