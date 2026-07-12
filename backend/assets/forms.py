from django import forms
from .models import Asset
from .models import AssetAllocation


class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset
        fields = "__all__"

        widgets = {

            "asset_tag": forms.TextInput(attrs={"class": "form-control"}),

            "name": forms.TextInput(attrs={"class": "form-control"}),

            "serial_number": forms.TextInput(attrs={"class": "form-control"}),

            "location": forms.TextInput(attrs={"class": "form-control"}),

            "acquisition_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "acquisition_cost": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "category": forms.Select(attrs={"class": "form-select"}),

            "department": forms.Select(attrs={"class": "form-select"}),

            "condition": forms.Select(attrs={"class": "form-select"}),

            "status": forms.Select(attrs={"class": "form-select"}),

            "image": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),

            "shared_bookable": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }


class AssetAllocationForm(forms.ModelForm):
    class Meta:
        model = AssetAllocation
        fields = [
            "asset",
            "employee",
            "expected_return_date",
        ]

        widgets = {

            "asset": forms.Select(attrs={
                "class": "form-select"
            }),

            "employee": forms.Select(attrs={
                "class": "form-select"
            }),

            "expected_return_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
        }        