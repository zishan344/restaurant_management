from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from account.models import Restaurant
from account.serializers import RestaurantSerializer
from account.models import Restaurant
from .serializers import RestaurantSerializer





@api_view(['POST'])
def staff_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if not username or not password:
        return Response(
            {"error":"Email and password are required"},
            status=status.HTTP_400_BAD_REQUEST
        )
    staff = authenticate(request, username=username, password=password)
    print(staff)
    if not staff:
        return Response({
            "error":"Invalid email or password"
        }, status=status.HTTP_401_UNAUTHORIZED)
    return Response({
        "message":"Login successfully",
        "staff_id":staff.id,
        "username":staff.username
    }, status=status.HTTP_200_OK)



""" class RestaurantView(ModelViewSet):
queryset = Restaurant.objects.all()
serializer_class = RestaurantSerializer  """

# TODO convert it single view use
@api_view(['POST'])
def create_restaurant(request):
    if request.method =="POST":
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
    elif request.method =="GET":
        pass
    elif request.method =="PUT":
        pass
    elif request.method == "DELETE":
        pass
    
"""     ''' 
    create restaurant data 
    '''
    serializer = RestaurantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"success",
        "data":serializer.data},status=status.HTTP_201_CREATED)
    return Response({"message":"error",
        "data":serializer.errors},status=status.HTTP_400_BAD_REQUEST) """

    

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