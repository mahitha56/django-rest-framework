from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
# Create your views here.
from students.models import Student
from .serializers import Studentserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
@api_view(['GET','POST'])
def studentview(req):
    if req.method=="GET":
      student=Student.objects.all() 
      serializer=Studentserializer(student,many=True)
      return Response(serializer.data,status=status.HTTP_200_OK)
    elif req.method=="POST":
       
       serializer=Studentserializer(data=req.data)
       if serializer.is_valid():
        
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
           
    
