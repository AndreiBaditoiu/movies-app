from django.http import HttpResponse
from django.shortcuts import render

import movies


# Create your views here.

def index(request):
    context = {
        'movies':['gladiator', 'terminator 2', 'contact' ]
    }
    return render(request, 'index.html', context )


def about(request):
    return render(request, 'about.html', {})

