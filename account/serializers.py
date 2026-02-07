from rest_framework.serializers import ModelSerializer
from models import Restaurant

class RestaurantSerializer(ModelSerializer):
    class Meta:
        model=Restaurant
        field= "__all__"