from django.db import transaction
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
import orders
from orders.models import Coupon, Order,Customer
from orders.serializers import OrderSerializer, CustomerSerializer
from orders.utils import validateDate

# Order view
class CustomerOrderListView(APIView):
    serializer_class = OrderSerializer # Standard naming convention

    def get(self, request):
        current_user = self.request.user
        customer_id = self.request.query_params.get("customer_id")

        # Logic for staff vs. regular users
        if current_user.is_staff and customer_id:
            queryset = Order.objects.filter(customer_id=customer_id)
        else:
            queryset = Order.objects.filter(user=current_user)

        # Serialize the data and return a Response object
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class CreateOrderView(APIView):
    def post(self, request):
        serializer = OrderSerializer(
            data= request.data,
        context = {'request':request}
        )

        if not serializer.is_valid():
            print("order serializer error")
            return Response({"validate":False,"error":serializer.errors},
            status= status.HTTP_400_BAD_REQUEST
            )
        with transaction.atomic():
            serializer.save()
        return Response({"validate": True, "data": serializer.data},
                        status=status.HTTP_201_CREATED)
# TODO complete it generate unique coupon
def CouponGenerate(request):
    pass

# coupon validation view
class CouponValidationView(APIView):
    def post(self, request):
        code = request.data.get()
        if not code:
            return Response({
                "error":"The 'code' field is required"
            }, status=status.HTTP_400_BAD_REQUEST)
        queryset = Coupon.objects.filter(code=code)
        if queryset.exists():
            data = queryset.first()
            is_active = data.is_active
            if(is_active and validateDate(
                data.valid_from,data.valid_until)):
                return Response({"valid":True, "message":"applied coupon successfully"},
                status=status.HTTP_200_OK)
            return Response({
                "valid":False,
                "error":"Invalid coupon"
            },status=HTTP_400_BAD_REQUEST)
        return Response({
            "valid":False,
            "error":"Invalid coupon code"
        }, status=status.HTTP_404_NOT_FOUND)

class CustomerListCreateView(APIView):
    def get(self, request):
        # Fetch and return all customers ordered by created_at descending
        queryset = Customer.objects.all().order_by('-created_at')
        serializer = CustomerSerializer(queryset, many=True)
        return Response(
            {"validate":True, "data":serializer.data},
            status=status.HTTP_200_OK
        )


    def post(self, request):
        # Validate and create a new customer
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'validate':True, 'data':serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(
            {'validate':False, error: serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )