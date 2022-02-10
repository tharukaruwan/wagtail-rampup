from django.db import models
from customer.models import Customer

# Customer order model
class CustomerOrder(models.Model):
    orderId=models.AutoField(primary_key=True)
    customer=models.ForeignKey(Customer,on_delete=models.DO_NOTHING,related_name='order',default='')
    orderCreatedDate=models.DateField()
    itemCount=models.IntegerField(blank=True)
    description=models.CharField(max_length=500,blank=True)
