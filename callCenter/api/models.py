
from django.db import models

# Create your models here.

class Customer(models.Model):
    firstName = models.CharField(max_length=200, null=False)
    lastName = models.CharField(max_length=200, null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address=models.CharField(max_length=300)
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=300)
    Country = models.CharField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.address

class Phone(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200, unique= True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)      
    def __str__(self):
        return self.phone