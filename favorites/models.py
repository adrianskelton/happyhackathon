from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib import messages
from affirmation.models import Affirmation

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    affirmation = models.ForeignKey(Affirmation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'affirmation')
    
    def clean(self):
        # Example validation: Ensure the user cannot favorite their own affirmation
        if self.user == self.affirmation.author:
            raise ValidationError("You cannot favorite your own affirmation.")

    def __str__(self):
        return f"{self.user.username}'s Favorite: {self.affirmation.text}"

@login_required
def add_to_favorites(request, affirmation_id):
    affirmation = get_object_or_404(Affirmation, pk=affirmation_id)
    
    # Try to get an existing favorite for the user and affirmation
    favorite, created = Favorite.objects.get_or_create(user=request.user, affirmation=affirmation)
    
    if created:
        # The affirmation was successfully added to favorites
        # You can add additional logic or messages here if needed
        messages.success(request, 'Affirmation added to favorites.')
    else:
        # The affirmation was already in the user's favorites
        # You can add a message or redirect to a different page if needed
        messages.info(request, 'Affirmation is already in favorites.')
    
    return redirect('home')  # Redirect to the home page or any other appropriate URL