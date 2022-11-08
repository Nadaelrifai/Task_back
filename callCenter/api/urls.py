from django.urls import path
from . import views
urlpatterns = [
    path('', views.getAllCustomer, name="customer"),
    path('getCustomerbyphone/<str:cus_phone>', views.getCustomerbyphone, name="getCustomerbyphone"),
    path('createCustomer/', views.createCustomer, name="createCustomer"),
    
]