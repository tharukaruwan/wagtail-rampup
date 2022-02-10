from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from customer.models import Customer
from customer.serializers import CustomerSerializer

from authServices.firebaseservices import registerUser, loginUser
from authServices.autherizatationservices import userAuthorization


@api_view(['POST','GET' ])
def apiCustomers(request):
    # signup
    if request.method == 'POST':
        # firebase register
        user=registerUser(request.data["email"],request.data["password"])
        if user["status"]=='error':
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        request.data["customerId"]=user["id"]
        customer_serializer=CustomerSerializer(data=request.data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            data={  'id':customer_serializer.data["customerId"],
                    'email':customer_serializer.data["email"],
                    'firstName':customer_serializer.data["firstName"],
                    'accessTocken':user["idToken"],
                    'refreshToken':user["refreshToken"] }
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(customer_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        customers= Customer.objects.all()
        customers_serializer=CustomerSerializer(customers,many=True)
        return Response(customers_serializer.data,status=status.HTTP_200_OK)

# Login customer
@api_view(['POST'])
def apiCustomerLogin(request):
    try:
        customer= Customer.objects.get(email=request.data["email"])
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    customer_serializer=CustomerSerializer(customer,many=False)
    user=loginUser(customer_serializer.data["email"],request.data["password"])

    data={  'id':customer_serializer.data["customerId"],
            'email':customer_serializer.data["email"],
            'firstName':customer_serializer.data["firstName"],
            'accessTocken':user["idToken"],
            'refreshToken':user["refreshToken"] }
    return Response(data,status=status.HTTP_200_OK)

# Protected route
@api_view(['GET','PUT','DELETE'])
def apiCustomer(request,id):
    # Protect route
    if userAuthorization(request.tocken,id)==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    try:
        customer= Customer.objects.get(customerId=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        customer_serializer=CustomerSerializer(customer,many=False)
        return Response(customer_serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        customer_serializer=CustomerSerializer(customer,data=request.data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return Response(customer_serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(customer_serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
