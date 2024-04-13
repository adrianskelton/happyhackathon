from django.contrib import admin
from django.urls import path, include
from affirmation.views import home, note
from profiles.views import view_profile
from django.conf.urls import handler404
from django.conf.urls import handler500
from django.views.defaults import page_not_found

handler404 = 'profiles.views.custom_404'
handler500 = 'profiles.views.custom_500'

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
    path('affirmation/', include('affirmation.urls')),
    path('profiles/', include('profiles.urls'))
]

# Define the custom 404 error handler function
def custom_404(request, exception):
    return page_not_found(request, exception, template_name='404.html')

# Define the custom 404 error handler function
def custom_500(request, exception):
    return page_not_found(request, exception, template_name='500.pug')

