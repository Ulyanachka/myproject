from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("hello, world!")

# def about(request):
#     return HttpResponse("About us")

import logging

from django.http import HttpResponse 

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return render(request, 'myapp/index.html')
def about(request):
    try:
        # some code that might raise an exception
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return render(request, 'myapp/about.html')
    else:
        logger.debug('About page accessed')
        return render (request, 'myapp/about.html')