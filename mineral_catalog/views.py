from django.shortcuts import render


def index(request):
    """Shows a welcome message and a link to view all minerals"""
    return render(request, 'index.html')
