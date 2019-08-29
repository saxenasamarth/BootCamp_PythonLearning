from django.db import models

# Create your models here.

class Section(models.Model):
	name=models.CharField(max_length=200)

class Student(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    age = models.IntegerField()