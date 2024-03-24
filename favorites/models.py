from django.db import models
from django.contrib.auth.models import User
from affirmation.models import Affirmation

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    affirmation = models.ForeignKey(Affirmation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'affirmation')
