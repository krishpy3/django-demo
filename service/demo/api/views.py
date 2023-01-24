from django.shortcuts import render
import os
from django.http import HttpResponse, JsonResponse

# Create your views here.


def home(request):
    
    return JsonResponse(dict(os.environ))
