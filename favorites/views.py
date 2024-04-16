from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Prefetch
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Favorite
from profiles.models import Profile
from affirmation.models import Affirmation, Category

@login_required
def add_to_favorites(request, category_slug, affirmation_id):
    affirmation = get_object_or_404(Affirmation, id=affirmation_id)
    category = get_object_or_404(Category, slug=category_slug)
    favorite, created = Favorite.objects.get_or_create(user=request.user, affirmation=affirmation, category=category)
    if created:
        messages.success(request, 'Affirmation added to favorites.')
    else:
        messages.info(request, 'Affirmation is already in favorites.')
    return redirect('favorites_page')

@login_required
def remove_from_favorites(request, favorite_id):
    favorite = get_object_or_404(Favorite, id=favorite_id)
    favorite.delete()
    messages.success(request, 'Favorite removed successfully.')
    return redirect('favorites_page')

@login_required
def favorite(request):
    # Get all favorite objects and prefetch related categories and affirmations
    favorites = Favorite.objects.filter(user=request.user).select_related('affirmation').prefetch_related('category')
    
    # Group favorites by category
    categories = {}
    for favorite in favorites:
        category = favorite.category
        if category not in categories:
            categories[category] = [favorite]
        else:
            categories[category].append(favorite)
    
    return render(request, 'favorite.html', {'categories': categories})