from django.urls import path
from .views import *



urlpatterns = [
    path('coupons/validate/',CouponValidationView.as_view(), name="coupon-validate"),
    path('history/',OrderView.as_view(), name="orders")
]