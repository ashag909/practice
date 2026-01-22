from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
import json

def welcome(request):
    output='<h1>This is server date and time {}</h2>'.format(datetime.datetime.today())
    response=HttpResponse(output)
    return response

def view1(request):
    emp={'empno':1,
         'ename':'Asha',
         'salary':50000}
    response=HttpResponse(str(emp))
    return response

def view2(request):
    student={'rollno':1,
             'name':'asha',
             'course':'python'}
    data=json.dumps(student)
    response=HttpResponse(data,content_type='appliation/json')
    return response