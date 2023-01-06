from django import forms
from .models import Table
from django.db.models import IntegerField, Model

from datetime import datetime
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator



class bookingForm(forms.ModelForm):

    # Validations
    name = forms.CharField(
        label='Full Name', min_length=3, max_length=50,
        validators=[RegexValidator(regex=r'^[a-zA-ZÀ-ÿ\s]*$',
        message='Only letters are allowed')],
        widget=forms.TextInput(
            attrs={'placeholder': 'John Dave'})
    )
    email = forms.EmailField(
        label='Email address', min_length=8, max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
        message='Put a valid email address!')],
        widget=forms.TextInput(
            attrs={'placeholder': 'email@gmail.com'})
    )
    guest = forms.IntegerField(
        label='Guests',
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ],
        help_text ="max number of guests you can invite is 10.",
        widget=forms.TextInput(
            attrs={'placeholder': 'Number of Guests?'}),
    )
    date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'min': datetime.now().date()}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    
    class Meta:
        model = Table
        fields = '__all__'
        