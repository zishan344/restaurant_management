from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemSerializer

@api_view(['POST'])
def create_menu_item(request):
    ''' create new item '''
    serializer = MenuItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status = status.HTTP_201_CREATED
            )
    return Response(
        {"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_menu_items(request):
    # TODO should be filter with restaurant id
    ''' List all available menu item '''
    items = MenuItem.objects.all()
    serializer = MenuItemSerializer(items, many=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
def get_menu_item(request, pk):
    ''' Retrive item by primary key '''
    item = get_object_or_404(MenuItem, pk=pk)
    serializer= MenuItemSerializer(item)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )

@api_view(['PUT'])
def update_menu_item(request, pk):
    ''' update item '''
    item = get_object_or_404(MenuItem, pk = pk)
    serializer = MenuItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(
        serializer.data,
        status = status.HTTP_400_BAD_REQUEST
    )
@api_view(['DELETE'])
def delete_menu_item(request, pk):
    ''' delete item with pk '''
    item = get_object_or_404(MenuItem, pk = pk)
    item.delete()
    return Response(
        status = status.HTTP_204_NO_CONTENT
    )
