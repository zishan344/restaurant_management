from django.db import models
# Create your models here.
# Menue category mdoel for food menu

class Restaurant(models.Model):
    # write your code here
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="RestaurantName"
    )
    owner_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Name"
    )
    email = models.EmailField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name="Email"
    )
    phone_number = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="ContactNumber"
    )
    address = models.TextField(
        null=False,
        blank=False,
        verbose_name="Address"
    )
    city = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="City"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="created time"
    )
    class Meta:
        # default ordering
        ordering = ['-created_at']


class MenuCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="CategoryName")
    # string represent
    def __str__(self):
        return self.name