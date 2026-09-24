from django.shortcuts import render,get_object_or_404
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

from rest_framework import mixins,generics,viewsets








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







# class Employees(APIView):
#   def get(self,request):
#     employe=Employe.objects.all()
#     serializer=Employeserializer(employe,many=True)
#     return Response(serializer.data,status=status.HTTP_200_OK)
#   def post(self,request):
#     serializer=Employeserializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data,status=status.HTTP_201_CREATED)
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)










# class Emdetail(APIView):
#   def get_object(self,pk):
#     try:
#       return Employe.objects.get(pk=pk)
#     except Employe.DoesNotExist:
#       raise Http404
#   def get(self,req,pk):
#     employ=self.get_object(pk)
#     serializer=Employeserializer(employ)
#     return Response(serializer.data,status=status.HTTP_200_OK)
#   def put(self,req,pk):
#     employe=self.get_object(pk)
#     serializer=Employeserializer(employe,data=req.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data,status=status.HTTP_200_OK)
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#   def delete(self,req,pk):
#     employe=self.get_object(pk)
#     employe.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
# """"






#mixins
# class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Employe.objects.all()
#     serializer_class=Employeserializer
#     def get(self,req):
#         return self.list(req)
#     def post(self,req):
#         return self.create(req)
# class Emdetail(generics.GenericAPIView):
#     pass





# generics
# class Employees(generics.ListAPIView,generics.CreateAPIView):
# class Employees(generics.ListCreateAPIView):
#     queryset=Employe.objects.all()
#     serializer_class=Employeserializer
# class Emdetail(generics.RetrieveAPIView):
#     pass



# class Employeviewset(viewsets.ViewSet):
#     def list(self,req):
#       querset=Employe.objects.all()
#       serializer=Employeserializer(querset,many=True)
#       return Response(serializer.data)
#     def create(self,req):
#       serializer=Employeserializer(data=req.data)
#       if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
#       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def retrieve(self,req,pk=None):
#       employe=get_object_or_404(Employe,pk=pk)
#       serializer=Employeserializer(employe)
#       return Response(serializer.data,status=status.HTTP_200_OK)
#     def update(self,req,pk=None):
#       employe=get_object_or_404(Employe,pk=pk)
#       serializer=Employeserializer(employe,data=req.data)
#       if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#       return Response(serializer.errors)
#     def delete(self,req,pk=None):
#       employe=get_object_or_404(Employe,pk=pk)
#       employe.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)
          


#using modelviewset
class Employeviewset(viewsets.ModelViewSet):
    queryset=Employe.objects.all()
    serializer_class=Employeserializer