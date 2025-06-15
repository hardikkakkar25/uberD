# models.py
from django.db import models
from django.contrib.auth.models import User

DAYS_OF_WEEK = [
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
    ('Sun', 'Sunday'),
]

class PricingConfig(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    days_applicable = models.JSONField(help_text="List of days this pricing applies to. e.g., ['Mon', 'Tue']")
    created_at = models.DateTimeField(auto_now_add=True)

    # Distance Base Price (fixed)
    base_price = models.FloatField()
    base_distance_km = models.FloatField()

    # Distance Additional Price
    additional_price_per_km = models.FloatField()

    # Waiting Charges
    free_wait_minutes = models.IntegerField(default=3)
    wait_charge_per_3min = models.FloatField()

    # Time Multiplier (related table)
    def __str__(self):
        return f"{self.name} ({'Active' if self.is_active else 'Inactive'})"

class TimeMultiplier(models.Model):
    config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE, related_name='time_multipliers')
    upper_limit_minutes = models.IntegerField()  # e.g. 60, 120, 180
    multiplier = models.FloatField()  # e.g. 1.0, 1.25, 2.2

    class Meta:
        ordering = ['upper_limit_minutes']

class ConfigChangeLog(models.Model):
    config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE)
    actor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    change_description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
