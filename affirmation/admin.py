from django.contrib import admin
from .models import Affirmation, Category
from favorites.models import Favorite

class AffirmationAdmin(admin.ModelAdmin):
    list_display = ('text', 'category', 'created_at', 'id')

admin.site.register(Affirmation, AffirmationAdmin)
admin.site.register(Favorite)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'icon']

admin.site.register(Category, CategoryAdmin)