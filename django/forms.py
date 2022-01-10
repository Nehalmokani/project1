from django import forms
from django.forms import fields
from .models import member

class memberform(forms.ModelForm):
    class Meta:
        model=member
        fields=['us','email','phn','password']
