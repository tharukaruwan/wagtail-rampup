from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet


class AdvertisementsPage(Page): # Template -> advertisements_page.html (_before uppercase and turn it into lower case)
    advertisement_title=models.CharField(max_length=100,default='Advertisement title')
    advertisement_description=models.CharField(max_length=500,default='Advertisement description')
    how_to_donate=models.CharField(max_length=500,default='How to donate')

    # helps to display in html page advertisement_page.html
    content_panels=Page.content_panels + [
        FieldPanel('advertisement_title'),
        FieldPanel('advertisement_description'),
        FieldPanel('how_to_donate'),
    ] 

# Just a python decarator to show snipets in admin panel
@register_snippet
class Card(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(blank=True,max_length=500)
    background_color=models.CharField(blank=True,max_length=100)
    learn_more_link=models.URLField(blank=True)
    # advertisement=models.ForeignKey(
    #     'Foreign.model',
    #     null=True,
    #     blank=False,
    #     on_delete=models.SET_NULL,
    #     related_name='+'
    # )

    # because this is just Django so panels
    # this helps to access cards in html pages
    panels=[
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('background_color'),
        FieldPanel('learn_more_link'),
        # FieldPanel('advertisement'),
    ]

    # return string representation of this class
    def __str__(self):
        return self.title
