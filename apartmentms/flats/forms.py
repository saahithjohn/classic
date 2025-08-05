from django import forms
from .models import Flat

class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        fields = ['number', 'uds_area', 'ownership_type', 'owner', 'tenant', 'is_occupied', 'occupancy_start', 'occupancy_end']
