from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'content', 'favorite_affirmations', 'emotion_emoji']