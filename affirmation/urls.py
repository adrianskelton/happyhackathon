from django.urls import path
from .views import affirmation, get_random_affirmation

urlpatterns = [
    # URL pattern for random affirmation without category
    path('affirmation/', affirmation, name='affirmation'),
    # URL pattern for affirmation with category
    path('affirmation/<slug:category_slug>/', affirmation, name='affirmation_by_category'),
    path('get_random_affirmation/', get_random_affirmation, name='get_random_affirmation'),
]