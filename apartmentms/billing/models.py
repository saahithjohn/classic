from django.db import models
from flats.models import Flat

class Bill(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='bills')
    month = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Bill for {self.flat} - {self.month}"
