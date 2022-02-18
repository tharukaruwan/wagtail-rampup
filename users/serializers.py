from rest_framework import serializers
from . import models

from authServices.firebaseservices import registerUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.User
        fields='__all__'
        extra_kwargs= {
            'password': {'write_only':True}
        }

    # def create(self,validated_data):
    #     print('validated_data=>',validated_data)
    #     user=registerUser(validated_data["email"],validated_data["password"])
    #     print('CREATED FIREBASE USER=>',user)
    #     password=validated_data.pop('password',None)
    #     instance=self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance
        