from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
import json

def welcome(request):
    output='<h1>This is server date and time {}</h2>'.format(datetime.datetime.today())
    response=HttpResponse(output)
    return response