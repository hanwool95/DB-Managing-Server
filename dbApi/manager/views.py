

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Todo need to set models
from .models import *


def index(request):
    return render(request, 'manager/index.html')


def create_concate_db(request):
    pass



def concate_db(request, number):
    if(request.method == "CREATE"):
        pass
