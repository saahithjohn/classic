from django.db import models
from residents.models import ResidentProfile

class Complaint(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField()
    resident = models.ForeignKey(ResidentProfile, on_delete=models.CASCADE, related_name='complaints')
    status = models.CharField(max_length=20, choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('closed', 'Closed')], default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject} ({self.status})"
