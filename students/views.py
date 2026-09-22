from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def students(req):
    students={
        'name' :'Mahitha',
        'age':20,
    }
    return HttpResponse(str(students))