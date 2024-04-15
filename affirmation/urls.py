from django.urls import path
from . import views
urlpatterns = [
    # URL pattern for random affirmation without category
    path('affirmation/', views.affirmation, name='affirmation'),
    # URL pattern for affirmation with category
    path('affirmation/<slug:category_slug>/', views.affirmation, name='affirmation_by_category'),
    path('get_random_affirmation/', views.get_random_affirmation, name='get_random_affirmation'),
    
    path('affirmation/<int:pk>/', views.affirmation, name='affirmation'),
    path('create/', views.create_affirmation, name='create_affirmation'),
    path('affirmation/<int:affirmation_id>/edit/', views.edit_affirmation, name='edit_affirmation'),
    path('affirmation/<int:affirmation_id>/delete/', views.delete_affirmation, name='delete_affirmation'),

    path('user_affirmations/', views.user_affirmation, name='user_affirmation'),
    path('user_affirmation/<int:user_affirmation_id>/edit/', views.edit_user_affirmation, name='edit_user_affirmation'),
    path('user_affirmation/<int:user_affirmation_id>/delete/', views.delete_user_affirmation, name='delete_user_affirmation'),

    path('profile/user_affirmations/', views.show_user_affirmation, name='profile_page'),

]