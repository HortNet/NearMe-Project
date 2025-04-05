from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello maza fazasi in there")

# Create your views here.
