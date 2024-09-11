from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class StudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'name']
    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)


