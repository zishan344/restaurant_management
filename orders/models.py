from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Category name")