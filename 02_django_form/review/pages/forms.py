from django import forms
from .models import Page

class Form(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content']
        
        