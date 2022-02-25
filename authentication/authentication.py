from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

from rest_framework import authentication
from rest_framework import exceptions

class userAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        print('SELF=>',self)
        print('REQUEST=>',request)
        return (None)
