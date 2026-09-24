
from rest_framework import serializers
from students.models import Student
from em.models import Employe


class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields= "__all__"

class Employeserializer(serializers.ModelSerializer):
    class Meta:
        model=Employe
        fields="__all__"