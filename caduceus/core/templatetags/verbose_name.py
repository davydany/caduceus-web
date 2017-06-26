from django import template
register = template.Library()

@register.simple_tag
def verbose_name(form, field_name):
    """
    Returns verbose_name for a field.
    """
    return form._meta.model._meta.get_field(field_name).verbose_name.title()