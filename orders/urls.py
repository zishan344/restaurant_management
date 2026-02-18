from django.urls import path
from .views import *



urlpatterns = [
    path('coupons/validate/',CouponValidationView.as_view(), name="coupon-validate"),
    path('customers/',CustomerListCreateView.as_view(), name="customers"),
    path('create/order/',CreateOrderView.as_view(), name="create_order")
    # path('history/',OrderView.as_view(), name="orders")
]