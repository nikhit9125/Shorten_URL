from django import template
from django.urls import reverse
 
register=template.Library()

@register.simple_tag
def redirect_url_with_short_code(shorten_url):
    url=reverse('redirect_to_original', args=[shorten_url])
    return url