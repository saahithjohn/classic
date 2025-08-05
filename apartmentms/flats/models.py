from django.db import models
from django.contrib.auth import get_user_model

class Flat(models.Model):
    number = models.CharField(max_length=10, unique=True)
    uds_area = models.DecimalField(max_digits=8, decimal_places=2)
    ownership_type = models.CharField(max_length=20, choices=[('owner', 'Owner'), ('tenant', 'Tenant')])
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owned_flats')
    tenant = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name='rented_flats')
    is_occupied = models.BooleanField(default=True)
    occupancy_start = models.DateField(null=True, blank=True)
    occupancy_end = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Flat {self.number}"
