from rest_framework import generics
from home.serializers import MenuCategorySerializer
from home.models import MenuCategory
from products.models import MenuItem
from products.serializers import MenuItemSerializer
# Create your views here.

class MenuCategoryView(generics.ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class FeaturedMenuView(generics.ListAPIView):
    queryset = MenuItem.objects.filter(is_featured=True)
    serializer_class=MenuItemSerializer