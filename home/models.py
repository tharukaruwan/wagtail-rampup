from tabnanny import verbose
from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    max_count=1 # only one home page
    # template='home/home_page.html' # explectly says where the template ans it's name, here its 'home_page.html' in 'home/home/templates' directory
    home_title=models.CharField(max_length=100,default='Home Page')
    home_description=models.CharField(max_length=100,default='Home Page Description')

    # helps to access in html and view in wagtail admin
    content_panels=Page.content_panels + [
        FieldPanel('home_title'),
        FieldPanel('home_description'),
    ]

    class Meta:
        verbose_name='Home Page' # Display name in admin panel for single
        verbose_name_plural='Home Pages' # Display name in admin panel for multiple pages
