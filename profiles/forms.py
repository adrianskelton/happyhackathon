from allauth.account.forms import SignupForm
from django import forms
from .models import Profile, Contact

class CustomSignUpForm(SignupForm):
    def __init__(self, *args, **kwargs):
      super(CustomSignUpForm, self).__init__(*args, **kwargs)
      self.error_class = DivErrorList

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'content', 'favorite_affirmations', 'emotion_emoji']


# ContactForm for handling contact information
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        # Customize widget attributes for name, email, and message fields
        self.fields['name'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your Email'
        self.fields['message'].widget.attrs['placeholder'] = 'Enter message ..'

    def clean_email(self):
        # Custom validation for the email field if needed
        email = self.cleaned_data.get('email')
        # Your validation logic here
        return email