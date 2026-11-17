from django import forms
from django.utils import timezone

from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["name", "contact", "preferred_date", "arrival_time", "party_size", "seating_preference", "notes"]
        widgets = {
            "preferred_date": forms.DateInput(attrs={"type": "date"}),
            "arrival_time": forms.TimeInput(attrs={"type": "time"}),
            "notes": forms.Textarea(attrs={"rows": 3}),
        }

    def clean_preferred_date(self):
        value = self.cleaned_data["preferred_date"]
        if value < timezone.localdate():
            raise forms.ValidationError("Please choose today or a future date.")
        return value


class AdminReservationForm(ReservationForm):
    class Meta(ReservationForm.Meta):
        fields = ReservationForm.Meta.fields + ["status"]
