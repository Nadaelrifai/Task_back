from rest_framework.serializers import ModelSerializer
from .models import *

class PhoneSerializer(ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class CustomerSerializer(ModelSerializer):
    phone_set = PhoneSerializer(many=True)
    address_set = AddressSerializer(many=True)
    class Meta:
        model = Customer
        fields = '__all__'

class CreateCustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'