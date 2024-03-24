from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('favorite/<int:affirmation_id>/', views.add_to_favorites, name='favorite'),
]