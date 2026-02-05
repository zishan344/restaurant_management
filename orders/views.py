from urllib import request, response
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response
from orders.models import Coupon
from orders.utils import validateDate

class CouponValidationView(APIView):
    def post(self, request):
        code = request.data.get('code')
        if not code:
            return Response(
                {"error":"The 'code' field is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        queryset = Coupon.objects.filter(code=code)
        
        if queryset.exists():
            data = queryset.first()
            is_active = data.is_active
        
            if is_active and validateDate(data.valid_from, data.valid_until):
                return Response(
                    {"valid":True, "message":"applied coupon successfully"},status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"valid":False, "error":"invalid coupon"},status=status.HTTP_200_OK
                )
        return Response({"valid":False, "error":"Invalid coupon code"}, status=status.HTTP_404_NOT_FOUND)



        