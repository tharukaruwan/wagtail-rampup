from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# user model manager
# overwrite create a new user
# overwrite create a superuser
class AccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        print('email=>',email)
        print('password=>',password)
        if not email:
            raise ValueError('Users must have an email')
        if not username:
            raise ValueError('Users must have an username')
        user=self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password=None):
        print('email=>',email)
        print('password=>',password)
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        return user

class Account(AbstractUser):
    email=models.EmailField(verbose_name='email',max_length=100,unique=True)
    username=models.CharField(max_length=30,unique=True)
    date_joined=models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login=models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    hide_email=models.BooleanField(default=True)

    object=AccountManager()

    # USERNAME_FIELD='email'
    # REQUIRED_FIELD=[]
    # REQUIRED_FIELD=['username']

    def __str__(self):
        return self.username
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    print('TOCKEN CREATING')
    print('sender=>',sender)
    print('sender.email=>',sender.email)
    print('sender.username=>',sender.username)
    print('sender.password=>',sender.password)
    if created:
        print('instance=>',instance)
        print('instance.email=>',instance.email)
        print('instance.password=>',instance.password)
        Token.objects.create(user=instance)
        print('TOCKEN CREATED')