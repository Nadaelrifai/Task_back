
from django.db import models

# Create your models here.

class Customer(models.Model):
    firstName = models.CharField(max_length=200, null=False)
    lastName = models.CharField(max_length=200, null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName, self.lastName

class Address(models.Model):
    address=models.CharField(max_length=300)
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=300)
    Country = models.CharField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

class phone(models.Model):
    phone = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)      