from django.urls import path
from . import views

urlpatterns = [
    path('favorites/add/<slug:category_slug>/<int:affirmation_id>/', views.add_to_favorites, name='favorites'),
    path('favorites/remove/<int:favorite_id>/', views.remove_from_favorites, name='remove_favorite'),
    path('favorites/', views.favorite, name='favorites_page'),
]