from django.contrib import admin
from .models import Affirmation, Category

class AffirmationAdmin(admin.ModelAdmin):
    list_display = ('text', 'category', 'created_at')  # Display the 'text' field in the admin list view

admin.site.register(Affirmation, AffirmationAdmin)
admin.site.register(Category) 