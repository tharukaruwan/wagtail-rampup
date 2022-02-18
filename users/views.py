from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

from authServices.firebaseservices import registerUser, loginUser
from authServices.autherizatationservices import userAuthorization

@api_view(['POST','GET' ])
def apiUsers(request):
    # signup
    if request.method == 'POST':
        # firebase register
        # user=registerUser(request.data["email"],request.data["password"])
        # if user["status"]=='error':
        #     return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # request.data["id"]=user["id"]
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={ 'email':serializer.data["email"] }
            # data={  'id':serializer.data["id"],
            #         'email':serializer.data["email"],
            #         'accessTocken':user["idToken"],
            #         'refreshToken':user["refreshToken"] }
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        user= User.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
