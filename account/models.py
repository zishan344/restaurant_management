from django.db import models

# Create your models here.
class Restaurant(models.Model):
    """ Restaurnt Model """
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
        verbose_name="Owner Name"
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
        verbose_name="Contact Number"
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
    has_delivery= models.BooleanField(
        default=True,
        verbose_name="Has Delivery"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="created At"
    )

    class Meta:
        # default ordering
        ordering = ['-created_at']
        verbose_name="Restaurant"
        verbose_name_plural="Restaurants"

    def __str__(self):
        return self.name