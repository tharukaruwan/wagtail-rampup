from django.urls import path
from customerOrder import views

urlpatterns=[
    path('orders',views.apiOrders,name='api-orders'),
    path('orders/<int:id>',views.apiOrder,name='api-order'),
]