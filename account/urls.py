from django.urls import path
from .views import *

urlpatterns = [
    path("staff/login/",staff_login, name="staff-login")
]