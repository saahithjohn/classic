from django import forms
from .models import AMCContract

class AMCContractForm(forms.ModelForm):
    class Meta:
        model = AMCContract
        fields = '__all__'
