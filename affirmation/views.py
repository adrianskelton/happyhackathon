import random
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Affirmation
from django.views.generic import ListView


def home(request):
    context = {}
    return render(request, "index.html", context)  

def note(request):
    context = {}
    return render(request, "note.html", context)  


# Category Views
class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'


def affirmation(request, category_slug=None):
    if category_slug:
        # Get category by slug
        category = Category.objects.get(slug=category_slug)
        # Get all affirmations in the specified category
        affirmations = category.affirmations.all()
    else:
        # Get all affirmations from all categories
        affirmations = Affirmation.objects.all()
    # Select a random affirmation from the filtered queryset
    random_affirmation = random.choice(affirmations)
    return render(request, 'affirmation.html', {'affirmation': random_affirmation})