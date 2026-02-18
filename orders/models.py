import uuid
from django.db import models
from django.contrib.auth import get_user_model
from products.models import MenuItem
# Create your models here.

User = get_user_model()

# order status
class OrderStatus(models.Model):
    # Defining choices for order status
    STATUSES = [
        ('PENDING','pending'),
        ('PROCESSING','processing'),
        ('COMPLETED','completed'),
        ('CANCELED','canceled'),
    ]
    name = models.CharField(
        max_length=50,
        unique=True,
        choices=STATUSES,
        default='PENDING',
        verbose_name="Status Name"
    )
    # string represent
    def __str__(self):
        return self.name


# Order model
class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders"
        )
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="customer"
    )
    """ status = models.ForeignKey(
        OrderStatus,
        on_delete=models.PROTECT, 
        verbose_name="Order Status",
        ) """
    status = models.CharField(default="PENDING", max_length=50)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At"
    )
    def __str__(self):
        return self.status


# customer model (optional for Dine-in or Guest Orders)
class Customer(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False,
        verbose_name="customer_id"
        )
    name = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        verbose_name="customer_name"
        )
    phone = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        verbose_name="customer_phone"
        )
    email = models.EmailField(
        null=True,
        blank=True,
        max_length=50,
        verbose_name="customer_Email"
        )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="customer_created_at"
        )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "customer_record"
    def __str__(self):
        return self.name or "Guest Customer"
    

# coupon model
class Coupon(models.Model):
    code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Coupon Code"
        )
    discount_percentage = models.DecimalField(
        decimal_places=2,
        max_digits=3,
        verbose_name="Coupon Discount"
        )
    is_active = models.BooleanField(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField()

    # represent string
    def __str__(self):
        return self.code

