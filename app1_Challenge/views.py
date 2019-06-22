from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_challenge(request):
    return HttpResponse("Hello World Challenge App")

