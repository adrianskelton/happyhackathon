from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm  #This still needs to be added

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