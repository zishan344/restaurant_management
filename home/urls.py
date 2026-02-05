from django.urls import path
from .views import *

urlpatterns = [
    path("menu_category/", MenuCategoryView.as_view(), name="menu-category")
]