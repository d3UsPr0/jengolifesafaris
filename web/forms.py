# forms.py
from django import forms

class QuotationForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name',
            'required': True
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Email',
            'required': True
        })
    )
    
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone',
            'required': True
        })
    )
    
    ADULT_CHOICES = [(i, str(i)) for i in range(1, 5)]
    adults = forms.ChoiceField(
        choices=ADULT_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'required': True
        })
    )
    
    CHILDREN_CHOICES = [(i, str(i)) for i in range(0, 4)]
    children = forms.ChoiceField(
        choices=CHILDREN_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'required': True
        })
    )
    
    arrival = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'required': True
        })
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Message',
            'required': True
        })
    )