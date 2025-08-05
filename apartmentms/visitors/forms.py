from django import forms
from .models import VisitorLog

class VisitorLogForm(forms.ModelForm):
    class Meta:
        model = VisitorLog
        fields = '__all__'
