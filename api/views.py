from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
# Create your views here.
from students.models import Student
from .serializers import Studentserializer,Employeserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from em.models import Employe
from django.http import Http404
# @api_view(['GET','POST'])
# def studentview(req):
#     if req.method=="GET":
#       student=Student.objects.all() 
#       serializer=Studentserializer(student,many=True)
#       return Response(serializer.data,status=status.HTTP_200_OK)
#     elif req.method=="POST":
       
#        serializer=Studentserializer(data=req.data)
#        if serializer.is_valid():
        
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
#        else:

#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET','PUT','DELETE'])
# def studientdetailview(req,pk):
#   try:
#     student=Student.objects.get(pk=pk)
#   except Student.DoesNotExist:
#     return Response(status=status.HTTP_404_NOT_FOUND)
#   if req.method=='GET':
#     serializer=Studentserializer(student)
#     return Response(serializer.data,status=status.HTTP_200_OK)
#   elif req.method=='PUT':
#     serializer=Studentserializer(student,data=req.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data,status=status.HTTP_201_CREATED)
#     else:
#       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#   elif req.method=='DELETE':
#     student.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)







class Employees(APIView):
  def get(self,request):
    employe=Employe.objects.all()
    serializer=Employeserializer(employe,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
  def post(self,request):
    serializer=Employeserializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)










class Emdetail(APIView):
  def get_object(self,pk):
    try:
      return Employe.objects.get(pk=pk)
    except Employe.DoesNotExist:
      raise Http404
  def get(self,req,pk):
    employ=self.get_object(pk)
    serializer=Employeserializer(employ)
    return Response(serializer.data,status=status.HTTP_200_OK)
  def put(self,req,pk):
    employe=self.get_object(pk)
    serializer=Employeserializer(employe,data=req.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  def delete(self,req,pk):
    employe=self.get_object(pk)
    employe.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
