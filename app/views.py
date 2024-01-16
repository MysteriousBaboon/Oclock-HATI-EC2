import logging

from django.shortcuts import render


logger = logging.getLogger('MONITORING')


def index(request):

    return render(request, 'index.html')

