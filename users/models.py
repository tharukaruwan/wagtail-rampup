from django.db import models
from django.contrib.auth.models import AbstractUser
from wagtail.snippets.models import register_snippet

@register_snippet 
class User(AbstractUser):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=255)
    username=models.CharField(max_length=255,unique=True)
    testattribute=models.CharField(max_length=255,default='test attribute')

    
    # USERNAME_FIELD='email'
    REQUIRED_FIELD=[]

