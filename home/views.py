from rest_framework import generics
from home.serializers import MenuCategorySerializer
from home.models import MenuCategory
# Create your views here.

class MenuCategoryView(generics.ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
