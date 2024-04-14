import random
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from .models import Category, Affirmation, AffirmationUser
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import AffirmationForm, UserAffirmationForm
import random
from django.contrib import messages



def home(request):
    # Retrieve an Affirmation object (or perform any logic to get the object)
    affirmation = Affirmation.objects.order_by('?').first()

    context = {'affirmation': affirmation}  # Include the affirmation object in the context
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


def create_affirmation(request):
    if request.method == 'POST':
        form = AffirmationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have successfully created an affirmation!')
            return redirect('home')  # Redirect to the home page after creating the affirmation
    else:
        form = AffirmationForm()
    return render(request, 'create_affirmation.html', {'form': form})

# # Edit affirmation view
def edit_affirmation(request, affirmation_id):
    affirmation = get_object_or_404(Affirmation, id=affirmation_id)
    if request.method == 'POST':
        form = AffirmationForm(request.POST, instance=affirmation)
        if form.is_valid():
            form.save()
            return redirect('affirmation_detail', affirmation_id=affirmation_id)
    else:
        form = AffirmationForm(instance=affirmation)
    return render(request, 'edit_affirmation.html', {'form': form, 'affirmation_id': affirmation_id})

# Delete affirmation view
def delete_affirmation(request, affirmation_id):
    affirmation = get_object_or_404(Affirmation, id=affirmation_id)
    if request.method == 'POST':
        affirmation.delete()
        return redirect('home')  # Redirect to home page after deletion
    return render(request, 'delete_affirmation.html', {'affirmation': affirmation})


@login_required
def user_affirmation(request):
    if request.method == 'POST':
        form = UserAffirmationForm(request.POST)
        if form.is_valid():
            affirmation = form.save(commit=False)
            affirmation.user = request.user  # Associate the affirmation with the logged-in user
            affirmation.save()
            messages.success(request, 'You have successfully created your affirmation!')
            return redirect(reverse('profile', kwargs={'username': request.user.username}))
    else:
        form = UserAffirmationForm()
    
    user_affirmations = AffirmationUser.objects.filter(user=request.user)   # Fetch affirmations created by the user
    
    return render(request, 'user_affirmation.html', {'form': form, 'user_affirmations': user_affirmations})

@login_required
def show_user_affirmations(request):
    user_affirmations = AffirmationUser.objects.filter(user=request.user)
    return render(request, 'profile.html', {'user_affirmations': user_affirmations})

@login_required
def edit_user_affirmation(request, user_affirmation_id):
    user_affirmation = get_object_or_404(AffirmationUser, id=user_affirmation_id)
    if request.method == 'POST':
        form = UserAffirmationForm(request.POST, instance=user_affirmation)
        if form.is_valid():
            form.save()
            return redirect('user_affirmation_detail', user_affirmation_id=user_affirmation_id)
    else:
        form = UserAffirmationForm(instance=user_affirmation)
    return render(request, 'edit_user_affirmation.html', {'form': form, 'user_affirmation_id': user_affirmation_id})

@login_required
def delete_user_affirmation(request, user_affirmation_id):
    user_affirmation = get_object_or_404(AffirmationUser, id=user_affirmation_id)
    if request.method == 'POST':
        user_affirmation.delete()
        return redirect('home')  # Redirect to home page after deletion
    return render(request, 'delete_user_affirmation.html', {'user_affirmation': user_affirmation})