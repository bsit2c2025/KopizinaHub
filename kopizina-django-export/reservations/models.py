from django.db import models


class Reservation(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]
    PARTY_CHOICES = [(str(i), f"{i} person" if i == 1 else f"{i} people") for i in range(1, 6)] + [("5+", "5+ people")]
    SEATING_CHOICES = [
        ("Quiet desk", "Quiet desk"),
        ("Shared table", "Shared table"),
        ("Any available seat", "Any available seat"),
    ]

    name = models.CharField(max_length=120)
    contact = models.CharField(max_length=160)
    preferred_date = models.DateField()
    arrival_time = models.TimeField()
    party_size = models.CharField(max_length=12, choices=PARTY_CHOICES)
    seating_preference = models.CharField(max_length=32, choices=SEATING_CHOICES, default="Any available seat")
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["preferred_date", "status"]), models.Index(fields=["contact"])]

    def __str__(self):
        return f"{self.name} — {self.preferred_date}"
