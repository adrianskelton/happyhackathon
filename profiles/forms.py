from allauth.account.forms import SignupForm
#from basic_django.utils import DivErrorList
from django import forms
from .models import Profile

class CustomSignUpForm(SignupForm):
    def __init__(self, *args, **kwargs):
      super(CustomSignUpForm, self).__init__(*args, **kwargs)
      self.error_class = DivErrorList

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'content', 'favorite_affirmations', 'emotion_emoji']