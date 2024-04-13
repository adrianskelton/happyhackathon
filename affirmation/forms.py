from django import forms
from .models import Affirmation, AffirmationUser

class AffirmationForm(forms.ModelForm):
    class Meta:
        model = Affirmation
        fields = ['text', 'category']
        labels = {
            'text': 'Affirmation Text',
            'category': 'Category',
        }


class UserAffirmationForm(forms.ModelForm):
    class Meta:
        model = AffirmationUser
        fields = ['text', 'category']
        labels = {
            'text': 'Affirmation Text',
            'category': 'Category',
        }