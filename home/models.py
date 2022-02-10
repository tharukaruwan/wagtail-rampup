from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    home_title=models.CharField(max_length=100,default='Home Page')
    home_description=models.CharField(max_length=100,default='Home Page Description')

    content_panels=Page.content_panels + [
        FieldPanel('home_title'),
        FieldPanel('home_description'),
    ]
