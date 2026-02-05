from django.db import models
# Create your models here.

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


class Order(models.Model):
    status = models.ForeignKey(
        OrderStatus,
        on_delete=models.CASCADE, 
        verbose_name="Order Status",
        )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At"
    )
    def __str__(self):
        return self.status.name


class Coupon(models.Model):
    code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Coupon Code"
        )
    discount_percentage = models.DecimalField(
        decimal_place=2,
        max_digits=3,
        verbose_name="Coupon Discount"
        )
    is_active = models.BooleanField(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField()

    # represent string
    def __str__(self):
        return self.code

