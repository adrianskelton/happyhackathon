from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Favorite
from affirmation.models import Affirmation

from django.contrib import messages

def add_to_favorites(request, affirmation_id):
    affirmation = get_object_or_404(Affirmation, pk=affirmation_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, affirmation=affirmation)
    if created:
        messages.success(request, 'Affirmation added to favorites successfully!')
    else:
        messages.info(request, 'Affirmation is already in favorites.')
    return redirect('affirmation', pk=affirmation_id)