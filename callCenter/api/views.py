from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *



# Create your views here.
@api_view(['GET'])
def getAllCustomer(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCustomerbyphone(request, cus_phone):
    phone = Phone.objects.filter(phone=cus_phone).select_related('customer')
    if phone:
        customer = phone[0].customer
        serializer = CustomerSerializer(customer, many=False)
        return Response(serializer.data)
          
    return Response("No customer found")

# @api_view(['POST'])
# def createCustomer(request):
#     data = request.data
#     customer = Customer.objects.create(
#         firstName=data['firstName'],
#         lastName=data['lastName']
#     )
#     serializer = CustomerSerializer(customer, many=False)
#     return Response(serializer.data)

@api_view(['POST'])
def createCustomer(request):
    data = request.data
    serializer = CreateCustomerSerializer(data=data)
    #serializer= PhoneSerializer(data=data['phone'])
    # serializer = AddressSerializer(data=data['address_set'])
    # SAVE CUSTOMER
    if serializer.is_valid():
        customer = serializer.save()
    # SAVE CUSTOMER PHONE NUMBERS
    obj = {'phone' : request.data['phone'], 'customer' : customer.id}
    serializer= PhoneSerializer(data= obj)
    if serializer.is_valid():
        serializer.save()

    # SAVE CUSTOMER ADDRESS
    obj1 = {
        'address' : request.data['address'],
        'zip_code' : request.data['zip_code'],
        'city' : request.data['city'],
        'Country' : request.data['Country'],
        'customer' : customer.id
        }
    serializer= AddressSerializer(data= obj1)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# {
#     "phone": "8888888",
#     "firstName": "Axam" ,
#     "lastName" : "ND",
#     "address" : "Akkar", 
#     "zip_code": "124",
#     "city": "Akkar",
#     "Country": "Lebanon"

# }
