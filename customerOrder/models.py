from django.db import models
from customer.models import Customer
from wagtail.snippets.models import register_snippet


# Just a python decarator to show snipets in admin panel
@register_snippet   # Customer order model
class CustomerOrder(models.Model):
    orderId=models.AutoField(primary_key=True)
    customer=models.ForeignKey(Customer,on_delete=models.DO_NOTHING,related_name='order',default='')
    orderCreatedDate=models.DateField()
    itemCount=models.IntegerField(blank=True)
    description=models.CharField(max_length=500,blank=True)

    # return string representation of this class
    def __str__(self):
        return self.orderId
