import random

from django.db.models.aggregates import Count
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404, render

from . import models


# List of names for order, and for skipping columns from the database not
# in this list
NAMES = [
    'group',
    'category',
    'formula',
    'strunz_classification',
    'color',
    'crystal_system',
    'unit_cell',
    'crystal_symmetry',
    'cleavage',
    'mohs_scale_hardness',
    'luster',
    'streak',
    'diaphaneity',
    'optical_properties',
    'refractive_index',
    'crystal_habit',
    'specific_gravity',
]


def mineral_list(request):
    """Shows the entire list of minerals"""
    minerals = models.Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals})


def mineral_detail(request, mineral_id):
    """Shows the detail view of a single mineral"""

    # Values is used instead of get to turn the output into a dictionary
    # This makes it possible to iterate through the key-value pair
    mineral = models.Mineral.objects.filter(id=mineral_id).values().first()
    prev_next = get_prev_next(mineral_id)
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral, 'names': NAMES, 'prev_next': prev_next})


# Note that a template tag version was successfully created to do this same
# function, but this version was chosen, as the template tag version hit the
# database on every page load, whereas this only hits the database when
# a random mineral is sought
def random_mineral(request):
    """Shows the detail view of a single random mineral"""

    # Gets random index based on the full count of minerals in the database
    count = models.Mineral.objects.aggregate(count=Count('id'))['count']
    random_index = random.randint(0, count - 1)

    # Get the values of the mineral by the random index
    mineral = models.Mineral.objects.all().values()[random_index]
    prev_next = get_prev_next(mineral.get('id'))
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral, 'names': NAMES, 'prev_next': prev_next})


def get_prev_next(mineral_id):
    """Generates a dictionary to provide the template the ID and name of the
    previous and next minerals alphabetically"""
    prev_mineral = (models.Mineral.objects
                    .filter(id__lt=mineral_id)
                    .exclude(id=mineral_id)
                    .order_by('-id')
                    .first())
    next_mineral = (models.Mineral.objects
                    .filter(id__gt=mineral_id)
                    .exclude(id=mineral_id)
                    .order_by('id')
                    .first())
    # Detects if the provided mineral ID is the first or last in the database
    # and sends the appropriate data if it's one of the ends
    if not prev_mineral:
        return {'next': {'id': next_mineral.id, 'name': next_mineral.name}}
    elif not next_mineral:
        return {'previous': {'id': prev_mineral.id, 'name': prev_mineral.name}}
    else:
        return {'next': {'id': next_mineral.id, 'name': next_mineral.name},
                'previous': {'id': prev_mineral.id, 'name': prev_mineral.name}}
