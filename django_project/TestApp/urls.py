from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from TestApp import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'sections', views.SectionViewSet)

urlpatterns = [    
    path('', include(router.urls)),
    url(r'^delete_student/$', views.delete_student),
]