from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
# Create your views here.

class StudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends=[OrderingFilter]
    ordering_fields = ['name', 'city']
   

