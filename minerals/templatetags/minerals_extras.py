import random

from django import template

from minerals.models import Mineral


register = template.Library()

# Not used in favor of handling random ID generation in the view, rather than
# through the template
"""
@register.simple_tag
def get_random_id():
    ids = Mineral.objects.all().values_list('id', flat=True)
    return random.choice(ids)
"""


@register.filter
def get_item(dictionary, key):
    """Adds the dictionary.get() function as a filter for the templates"""
    return dictionary.get(key)


@register.filter
def rem_underscore(string):
    """Removes underscores from a string and replaces with a space"""
    return string.replace('_', ' ')
