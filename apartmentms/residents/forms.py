from django import forms
from .models import ResidentProfile

class ResidentProfileForm(forms.ModelForm):
    class Meta:
        model = ResidentProfile
        fields = ['user', 'flat', 'phone', 'email', 'communication_pref', 'is_owner', 'is_tenant', 'move_in_date', 'move_out_date']
