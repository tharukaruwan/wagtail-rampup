from django.db import models
from django.contrib.auth.models import AbstractUser
from wagtail.snippets.models import register_snippet

from authServices.firebaseservices import registerUser
from django.db.models.signals import pre_save, post_save

@register_snippet 
class User(AbstractUser):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=255)
    username=models.CharField(max_length=255,unique=True)
    testattribute=models.CharField(max_length=255,default='test attribute')

    
    # USERNAME_FIELD='email'
    REQUIRED_FIELD=[]

    def save(self, *args, **kwargs):
        # print('NEW MODEL self.email=>',self.email)
        # print('NEW MODEL self.password=>',self.password)
        super().save(*args, **kwargs)  # Call the "real" save() method.
        # print('NEW MODEL args =>',args)
        # print('NEW MODEL kwargs =>',kwargs)

def user_pre_save(sender,instance,*args, **kwargs):
    print('pre_save')
    # print(args,kwargs)
    # print(sender,instance)
    # print('NEW MODEL instance.email =>',instance.email)
    # print('NEW MODEL instance.password =>',instance.password)

pre_save.connect(user_pre_save,sender=User)

def user_post_save(sender,instance,*args, **kwargs):
    print('post_save')
    print('NEW MODEL instance =>',instance)
    print('NEW MODEL instance.email =>',instance.email)
    print('NEW MODEL instance.password =>',instance.password)
    # print(args,kwargs)

post_save.connect(user_post_save,sender=User)
    

