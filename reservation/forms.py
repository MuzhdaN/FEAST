from django import forms
from .models import Table


class bookingForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = '__all__'
        