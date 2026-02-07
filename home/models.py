from django.db import models
# Create your models here.
# Menue category mdoel for food menu


class MenuCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="CategoryName")
    # string represent
    def __str__(self):
        return self.name