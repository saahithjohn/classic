from django.db import models

class VisitorLog(models.Model):
    name = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    contact = models.CharField(max_length=20, blank=True)
    blacklist = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.purpose})"
