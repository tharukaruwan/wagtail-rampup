from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status

import account

from .models import Account
from .serializers import AccountSerializer

# rest tocken imports
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

# rest tocken permissions imports
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from authServices.firebaseservices import registerUser, loginUser
from authServices.autherizatationservices import userAuthorization


# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])

@api_view(['POST'])
def apiRegisterUsers(request):
    print('REGISTERING!')
    # signup
    if request.method == 'POST':
        # firebase register
        # user=registerUser(request.data["email"],request.data["password"])
        # if user["status"]=='error':
        #     return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # request.data["customerId"]=user["id"]
        serializer=AccountSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            data={  'id':serializer.data["id"],
                    'email':serializer.data["email"],
                    'username':serializer.data["username"],
                    'token':token.key }
            # data={  'id':serializer.data["id"],
            #         'email':serializer.data["email"],
            #         'username':serializer.data["username"],
            #         'token':token }
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# Login customer
# @api_view(['POST'])
# def apiLoginUsers(request):
#     try:
#         customer= Account.objects.get(email=request.data["email"])
#     except Account.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     serializer=AccountSerializer(customer,many=False)
#     # user=loginUser(serializer.data["email"],request.data["password"])

#     data={  'id':serializer.data["customerId"],
#             'email':serializer.data["email"],
#             'firstName':serializer.data["firstName"],
#             'accessTocken':user["idToken"],
#             'refreshToken':user["refreshToken"] }
#     return Response(data,status=status.HTTP_200_OK)
    