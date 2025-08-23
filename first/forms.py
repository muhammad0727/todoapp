from django import forms
from django.utils import timezone
from .models import List
class ListForm(forms.ModelForm):
    
    class Meta:
        model = List
        fields = ("title",'description','completed')
