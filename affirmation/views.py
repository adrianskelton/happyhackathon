import random
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Affirmation
from django.views.generic import ListView
import random


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

def get_random_affirmation(request):
    if request.method == 'POST':
        # Handle POST request to get a random affirmation
        category_name = request.POST.get('category')
        try:
            category = Category.objects.get(title=category_name)
            affirmations = category.affirmations.all()
            if affirmations:
                random_affirmation = random.choice(affirmations)
                return render(request, 'note.html', {'affirmation': random_affirmation})
            else:
                return render(request, 'note.html', {'affirmation': None})
        except Category.DoesNotExist:
            return HttpResponse("Category does not exist")
    else:
        # Handle GET request to render the form with categories
        categories = Category.objects.all()
        return render(request, 'select_category.html', {'categories': categories})