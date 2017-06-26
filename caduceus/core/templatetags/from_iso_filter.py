import arrow
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='from_iso')
@stringfilter
def from_iso(iso_string):
    """
    Returns verbose_name for a field.
    """
    return arrow.get(iso_string).datetime