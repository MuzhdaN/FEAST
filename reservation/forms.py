from django import forms
from .models import Table


class reserveTableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = '__all__'
        