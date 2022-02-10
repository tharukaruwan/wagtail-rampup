from django.db import models

# Customerr model
class Customer(models.Model):
    customerId=models.CharField(primary_key=True,max_length=500)
    email=models.EmailField(blank=False,null=False)
    firstName=models.CharField(max_length=500)
    lastName=models.CharField(max_length=500,blank=True)
    dateOfBirth=models.DateField()
    currencyBalance=models.FloatField()
    pageVisitors=models.IntegerField(blank=True)
