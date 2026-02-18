from rest_framework.serializers import ModelSerializer
from orders.models import Order, Customer

class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id', 'name','phone', 'email', 'created_at']

        # handle optional field
        extra_kwargs = {
            'name':{'required':False, 'allow_null':True, 'allow_blank':True},
            'phone':{'required':False, 'allow_null':True, 'allow_blank':True},
            'email':{'required':False, 'allow_null':True, 'allow_blank':True}
        }


class OrderSerializer(ModelSerializer):
    customer = CustomerSerializer(required=False)
    class Meta:
        model = Order
        fields ='__all__'
    def create(self, validate_data):
        customer_data = validate_data.pop('customer',None)
        if customer_data:
            print("error boss")
            guest_customer = Customer.objects.create(**customer_data)
            validate_data['customer'] = guest_customer
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validate_data['user'] = request.user
        return Order.objects.create(**validate_data)