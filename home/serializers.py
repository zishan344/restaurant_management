from rest_framework.serializers import ModelSerializer
from home.models import MenuCategory

class MenuCategorySerializer(ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ["name"]