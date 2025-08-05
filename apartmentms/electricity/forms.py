from django import forms
from .models import ElectricityUsage

class ElectricityUsageForm(forms.ModelForm):
    class Meta:
        model = ElectricityUsage
        fields = '__all__'
