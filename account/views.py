from rest_framework.decorators import api_view #, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status

# import account

# from .models import Account
from .serializers import AccountSerializer

# rest tocken imports
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

# rest tocken permissions imports
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from authServices.firebaseservices import registerUser, loginUser
from authServices.autherizatationservices import userAuthorization

import boto3

import hmac, hashlib, base64


# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])

@api_view(['POST'])
def apiRegisterUsers(request):
    if request.method == 'POST':

        serializer=AccountSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            
            username = serializer.data["email"]
            app_client_id = 'app_client_id'
            key = 'key'
            message = bytes(username+app_client_id,'utf-8')
            key = bytes('key','utf-8')
            secret_hash = base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha256).digest()).decode()

            client = boto3.client(
                'cognito-idp', 
                region_name='ap-southeast-1',
                aws_access_key_id='aws_access_key_id',
                aws_secret_access_key='aws_secret_access_key',
                )
            response = client.sign_up(
                ClientId='ClientId',
                SecretHash=secret_hash,
                # Email=serializer.data["email"],
                Username=serializer.data["email"],
                Password=serializer.data["password"],
                UserAttributes = [
                    { "Name": "email", "Value": serializer.data["email"] }
                ],
            )
            # REST TOCKEN
            # token, created = Token.objects.get_or_create(user=user)
            # data={  'id':serializer.data["id"],
            #         'email':serializer.data["email"],
            #         'username':serializer.data["username"],
            #         'token':token.key }
            return Response(response,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def apiUserVerification(request):
    if request.method == 'POST':

        confirmationCode=request.data["confirmationCode"]
        Username=request.data["email"]

        client = boto3.client(
                'cognito-idp', 
                region_name='ap-southeast-1',
                aws_access_key_id='aws_access_key_id',
                aws_secret_access_key='aws_secret_access_key',
            )

        app_client_id = 'app_client_id'
        key = 'key'
        message = bytes(Username+app_client_id,'utf-8')
        key = bytes('key','utf-8')
        secret_hash = base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha256).digest()).decode()

        response = client.confirm_sign_up(
            ClientId='ClientId',
            SecretHash=secret_hash,
            Username=Username,
            ConfirmationCode=confirmationCode,
            ForceAliasCreation=False,
        )
        return Response(response,status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def apiUserLogin(request):
    if request.method == 'POST':

        password=request.data["password"]
        Username=request.data["email"]

        client = boto3.client(
                'cognito-idp', 
                region_name='ap-southeast-1',
                aws_access_key_id='aws_access_key_id',
                aws_secret_access_key='aws_secret_access_key',
            )

        app_client_id = 'app_client_id'
        key = 'key'
        message = bytes(Username+app_client_id,'utf-8')
        key = bytes('key','utf-8')
        secret_hash = base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha256).digest()).decode()

        response = client.initiate_auth(
            ClientId='ClientId',
            AuthFlow='USER_PASSWORD_AUTH',
            # SecretHash=secret_hash,
            AuthParameters={
                'USERNAME': Username,
                'PASSWORD': password,
                "SECRET_HASH": secret_hash
            },
        )

        return Response(response,status=status.HTTP_200_OK)
    