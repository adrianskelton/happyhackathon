from django.db import models
from django.template.defaultfilters import slugify

# Model representing a category for blog posts
class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    icon = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Affirmation(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='affirmations', default=None)

    def __str__(self):
        return self.text