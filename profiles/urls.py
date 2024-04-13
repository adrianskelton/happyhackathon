from . import views
from django.urls import path, include

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('404/', views.custom_404, name='404'),
    path('500/', views.custom_500, name='500'),

    path('<username>/', views.ProfileDetailView.as_view(), name='profile'),
    path('create_profile/', views.CreateProfileView.as_view(), name='create_profile'),
    path('profile/edit_profile/', views.EditProfileView.as_view(), name='edit_profile'),
]