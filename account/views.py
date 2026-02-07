from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from account.models import Restaurant
from account.serializers import RestaurantSerializer
# Create your views here.

""" class RestaurantView(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer """

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant
from .serializers import RestaurantSerializer

@api_view(['POST'])
def create_restaurant(request):
    ''' 
    create restaurant data 
    '''
    serializer = RestaurantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"success",
        "data":serializer.data},status=status.HTTP_201_CREATED)
    return Response({"message":"error",
        "data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    

@api_view(['GET'])
def list_restaurants(request):
    ''' 
    getting all restaurant list 
    '''
    restaurant = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurant,many=True)
    return Response({"message":"success",
                      "data":serializer.data
                    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_restaurant(request, pk):
    ''' 
    get restaurant details 
    '''
    restaurant = get_object_or_404(Restaurant, pk=pk)
    serializer = RestaurantSerializer(restaurant)
    return Response({"message":"success",
     "data":serializer.data}, status=status.HTTP_200_OK)
     
@api_view(['PUT'])
def update_restaurant(request, pk):
    ''' 
    update restaurant details 
    '''
    restaurant = get_object_or_404(Restaurant,pk=pk)
    serializer = RestaurantSerializer(restaurant, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"success",
            "data":serializer.data}, status=status.HTTP_200_OK)
    return Response({"message":"error",
                    "data": serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_restaurant(request, pk):
    ''' 
    delete restaurant 
    '''
    restaurant = get_object_or_404(Restaurant,pk=pk)
    restaurant.delete()
    return Response({"message":"success"}, status=status.HTTP_204_NO_CONTENT)