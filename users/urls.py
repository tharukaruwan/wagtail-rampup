from django.urls import path
from . import views

urlpatterns=[
    path('register',views.apiUsers,name='api-users'),
    # path('customer/login',views.apiCustomerLogin,name='api-customer-login'),
    # path('customers/<str:id>',views.apiCustomer,name='api-customer'),
]