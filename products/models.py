from django.db import models
from account.models import Restaurant
# Create your models here.
from django.db import models
from .models import Restaurant  # Make sure this import path is correct

class MenuItem(models.Model):
    ''' 
    restaurant menu item
    '''
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="menu_items", 
        verbose_name="restaurant"      
        )
    name = models.CharField(
        max_length=150,
        verbose_name = "item_name",
        )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="item_description"
        )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2, 
        verbose_name="price"
        )
    is_available = models.BooleanField(
        default=True,
        verbose_name="available_item")
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="created_date"
        )
    
    def __str__(self):
        return str(self.name)