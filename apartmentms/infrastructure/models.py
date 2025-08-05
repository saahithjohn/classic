from django.db import models

class AMCContract(models.Model):
    name = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    contact = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.vendor})"
