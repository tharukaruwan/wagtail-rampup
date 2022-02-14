from django import template
from advertisements.models import Card

register = template.Library()

@register.inclusion_tag('advertisements/tags/advertisements.html', takes_context=True)
def advertisements(context):
    return {
        'advertisements': Card.objects.all(),
        'request': context['request'],
    }