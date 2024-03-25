from django import forms
from .models import Affirmation

class AffirmationForm(forms.ModelForm):
    class Meta:
        model = Affirmation
        fields = ['text', 'category']  # Define fields you want to include in the form
        labels = {
            'text': 'Affirmation Text',  # Customize field labels if needed
            'category': 'Category',  # Customize field labels if needed
        }
