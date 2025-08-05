from django.db import models
from django.contrib.auth import get_user_model
from flats.models import Flat

class ResidentProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='resident_profile')
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='residents')
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    communication_pref = models.CharField(max_length=20, choices=[('email', 'Email'), ('whatsapp', 'WhatsApp')], default='email')
    is_owner = models.BooleanField(default=False)
    is_tenant = models.BooleanField(default=False)
    move_in_date = models.DateField(null=True, blank=True)
    move_out_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.flat.number})"
