from django.contrib import admin
from .models import Favorite

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('category', 'affirmation_text', 'created_at')

    def affirmation_text(self, obj):
        return obj.affirmation.text

    def category(self, obj):
        return obj.affirmation.category.title if obj.affirmation.category else None

    affirmation_text.short_description = 'Affirmation Text'
    category.short_description = 'Category'

admin.site.register(Favorite, FavoriteAdmin)