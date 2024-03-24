from django.contrib import admin
from django.urls import path, include
from affirmation.views import home, note
from profiles.views import view_profile

from accounts.views import (
    login_view, 
    logout_view,
    register_view,
    view_profile,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('note/', note, name='note'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

    path('profile/', view_profile, name='view_profile'),
    path('', include('affirmation.urls')),
]

