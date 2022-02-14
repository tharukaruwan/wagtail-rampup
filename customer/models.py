from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel

# from django import template

# register = template.Library()

# Just a python decarator to show snipets in admin panel
@register_snippet
class Customer(models.Model):   # Customerr model
    customer_id=models.CharField(primary_key=True,max_length=500)   # _ helps to set a space in wagtail admin panel
    email=models.EmailField(blank=False,null=False)
    first_name=models.CharField(max_length=500)
    last_name=models.CharField(max_length=500,blank=True)
    date_of_birth=models.DateField()
    currency_balance=models.FloatField()
    page_visitors=models.IntegerField(blank=True)

    # Helps to access in html pages
    panels=[
        FieldPanel('customer_id'),
        FieldPanel('email'),
        FieldPanel('first_name'),
        FieldPanel('last_name'),
        FieldPanel('date_of_birth'),
        FieldPanel('currency_balance'),
        FieldPanel('page_visitors'),
    ]

    # return string representation of this class
    def __str__(self):
        return self.first_name

# Advert snippets
# @register.inclusion_tag('home/templates/home/home_page.html', takes_context=True)
# def customers(context):
#     return {
#         'customer': Customer.objects.all(),
#         'request': context['request'],
#     }