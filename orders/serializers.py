from rest_framework.serializers import ModelSerializer
from orders.models import Order, Customer

class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = ['id','phone', 'email', 'created_at']

        # handle optional field
        extra_kwargs = {
            'name':{'required':False, 'allow_null':True, 'allow_blank':True},
            'phone':{'required':False, 'allow_null':True, 'allow_blank':True},
            'email':{'required':False, 'allow_null':True, 'allow_blank':True}
        }


class CustomerSerializer(ModelSerializer):
    
    class Meta:
        model = Customer
        fields ='__all__'