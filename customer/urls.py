from django.urls import path
from customer import views

urlpatterns=[
    path('customers',views.apiCustomers,name='api-customers'),
    path('customer/login',views.apiCustomerLogin,name='api-customer-login'),
    path('customers/<str:id>',views.apiCustomer,name='api-customer'),
]