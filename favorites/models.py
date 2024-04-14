from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib import messages
from affirmation.models import Affirmation, Category

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    affirmation = models.ForeignKey(Affirmation, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'affirmation')

    def __str__(self):
        return f"{self.user.username}'s Favorite: {self.affirmation.text}"