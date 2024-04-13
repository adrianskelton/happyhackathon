from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from affirmation.models import Affirmation  

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    favorite_affirmations = models.ManyToManyField(Affirmation, blank=True)  
    EMOTION_CHOICES = [
        ('happy', '😊'),
        ('sad', '😢'),
        ('angry', '😠'),
        ('love', '❤️'),
        # these can be changed later?
    ]
    emotion_emoji = models.CharField(max_length=255, choices=EMOTION_CHOICES, blank=True, null=True)

    class Meta: 
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"
    
    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.owner.username})

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

# Model to store contact form informations.
class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField()
    name = models.CharField(max_length=50, )

    def __str__(self):
        return self.email
