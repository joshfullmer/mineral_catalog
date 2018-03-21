import random

from django import template

from minerals.models import Mineral


register = template.Library()


@register.simple_tag
def get_random_id():
    ids = Mineral.objects.all().values_list('id', flat=True)
    return random.choice(ids)


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def rem_underscore(string):
    return string.replace('_', ' ')
