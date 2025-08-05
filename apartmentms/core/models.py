from django.db import models
from residents.models import ResidentProfile

class Message(models.Model):
    subject = models.CharField(max_length=100)
    body = models.TextField()
    sender = models.ForeignKey(ResidentProfile, on_delete=models.SET_NULL, null=True, related_name='sent_messages')
    recipient = models.ForeignKey(ResidentProfile, on_delete=models.SET_NULL, null=True, related_name='received_messages')
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
