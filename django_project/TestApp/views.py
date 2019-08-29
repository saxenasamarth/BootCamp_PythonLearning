from django.shortcuts import render

# Create your views here.

from .models import *
from .serializers import *
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination
import rest_framework.generics as generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
# Create your views here.
class JSONResponse(HttpResponse):
   """
   An HttpResponse that renders its content into JSON.
   """
   def __init__(self, data, **kwargs):
       content = JSONRenderer().render(data)
       kwargs['content_type'] = 'application/json'
       super(JSONResponse, self).__init__(content, **kwargs)


class SectionViewSet(viewsets.ModelViewSet):
   queryset = Section.objects.all().order_by('-id')
   serializer_class = Section_Serializer

class StudentViewSet(viewsets.ModelViewSet):
   queryset = Student.objects.all().order_by('-id')
   serializer_class = Student_Serializer


@csrf_exempt
def delete_student(request):
	if request.method == 'POST':
		student = request.POST["name"]
		Student.objects.filter(name=student).delete()
		#return JSONResponse("Deleted", status=200)
		students=Student.objects.all().order_by('name')
		serializer=Student_Serializer(students,many=True)
		return JSONResponse(serializer.data, status=200)


