from django import template
from customer.models import Customer

register = template.Library()

@register.inclusion_tag('customer/tags/customers.html', takes_context=True)
def customers(context):
    return {
        'customers': Customer.objects.all(),
        'request': context['request'],
    }