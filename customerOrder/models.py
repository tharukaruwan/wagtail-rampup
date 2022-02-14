from django.db import models
from customer.models import Customer
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel


# Just a python decarator to show snipets in admin panel
@register_snippet   # Customer order model
class CustomerOrder(models.Model):
    # order_id=models.AutoField(primary_key=True,auto_created=True) # _ helps to set a space in wagtail admin panel
    order_id=models.CharField(primary_key=True,max_length=500) 
    customer=models.ForeignKey(Customer,on_delete=models.DO_NOTHING,related_name='order',default='')
    order_created_date=models.DateField()
    item_count=models.IntegerField(blank=True)
    description=models.CharField(max_length=500,blank=True)

    # Helps to access in html pages
    panels=[
        FieldPanel('order_id'),
        FieldPanel('customer'),
        FieldPanel('order_created_date'),
        FieldPanel('item_count'),
        FieldPanel('description'),
    ]

    # return string representation of this class
    def __str__(self):
        return self.order_id
