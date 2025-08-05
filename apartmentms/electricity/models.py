from django.db import models
from flats.models import Flat

class ElectricityUsage(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='electricity_usages')
    month = models.CharField(max_length=20)
    units = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.flat} - {self.month}: {self.units} units"
