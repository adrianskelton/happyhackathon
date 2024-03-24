from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm, ContactForm
from django.contrib import messages

def view_profile(request):
    user = request.user
    profile = Profile.objects.get(owner=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form})


# View function for a contact form.
def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


# View function for a successfully sent contact form.
def success(request):
    return render(request, 'success.html')