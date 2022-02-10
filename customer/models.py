from django.db import models
from wagtail.snippets.models import register_snippet

# Just a python decarator to show snipets in admin panel
@register_snippet
class Customer(models.Model):   # Customerr model
    customerId=models.CharField(primary_key=True,max_length=500)
    email=models.EmailField(blank=False,null=False)
    firstName=models.CharField(max_length=500)
    lastName=models.CharField(max_length=500,blank=True)
    dateOfBirth=models.DateField()
    currencyBalance=models.FloatField()
    pageVisitors=models.IntegerField(blank=True)

    # return string representation of this class
    def __str__(self):
        return self.firstName
