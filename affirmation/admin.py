from django.contrib import admin
from .models import Affirmation, Category, AffirmationUser

class AffirmationAdmin(admin.ModelAdmin):
    list_display = ('text', 'category', 'created_at', 'id')

admin.site.register(Affirmation, AffirmationAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'icon']

admin.site.register(Category, CategoryAdmin)

class AffirmationUserAdmin(admin.ModelAdmin):
    list_display = ('text', 'category', 'created_at', 'id')

admin.site.register(AffirmationUser, AffirmationUserAdmin)
