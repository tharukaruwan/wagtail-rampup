from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from customerOrder.models import CustomerOrder
from customerOrder.serializers import CustomerOrderSerializer

from authServices.autherizatationservices import orderViewAuthorization

@api_view(['POST','GET' ])
def apiOrders(request):
    if request.method == 'POST':
        # verify 
        if request.tocken=='':
           return Response(status=status.HTTP_401_UNAUTHORIZED) 
        request.data["customer"]=request.tocken["user_id"]
        order_serializer=CustomerOrderSerializer(data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(order_serializer.data,status=status.HTTP_201_CREATED)
        return Response(order_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        orders= CustomerOrder.objects.all()
        print(orders)
        # return Response(status=status.HTTP_200_OK)
        orders_serializer=CustomerOrderSerializer(orders,many=True)
        return Response(orders_serializer.data,status=status.HTTP_200_OK)

@api_view(['GET','PUT','DELETE'])
def apiOrder(request,id):
    try:
        order= CustomerOrder.objects.get(orderId=id)
    except CustomerOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    order_serializer=CustomerOrderSerializer(order,many=False)
    # Protect route
    if orderViewAuthorization(request.tocken,order_serializer.data)==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        return Response(order_serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        order_serializer=CustomerOrderSerializer(order,data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(order_serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(order_serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
