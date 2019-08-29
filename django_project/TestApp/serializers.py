from rest_framework import serializers
from .models import *

class Student_Serializer(serializers.ModelSerializer):
   class Meta:
       model = Student
       fields = '__all__'

class Section_Serializer(serializers.ModelSerializer):
   class Meta:
       model = Section
       fields = '__all__'