# main/forms.py

from django import forms
from .models import UrlData

class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlData
        fields = ['url']
        widgets = {
            'url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://ornek.com/uzun-adresinizi-buraya-yapistirin'
            })
        }
        labels = {
            'url': ''
        }