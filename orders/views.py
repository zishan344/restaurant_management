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
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes = [IsAuthenticated]
    

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

class CustomerView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer