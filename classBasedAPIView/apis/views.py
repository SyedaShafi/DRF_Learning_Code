from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class StudentAPI(APIView):
    def get(self, request, id=None, format=None):
        if id is not None:
            stu_obj = Student.objects.get(id=id)
            serializer = StudentSerializer(stu_obj)
            return Response(serializer.data)
        
        stu_objs = Student.objects.all()
        serializer = StudentSerializer(stu_objs, many=True )
        return Response(serializer.data) 

    def post(self, request, format=None):
        data = request.data
        serialize = StudentSerializer(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({'msg': 'Data Created'}, status = status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None, format=None):
        data = request.data
        # id = request.data.get('id')
        student_obj = Student.objects.get(id=id)
        serialize = StudentSerializer(student_obj, data = data)

        if serialize.is_valid():
            serialize.save()
            return Response({'msg': 'Complete Data updated!'}, status=status.HTTP_200_OK)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None, format=None):
        data = request.data
        student_obj = Student.objects.get(id=id)
        serialize = StudentSerializer(student_obj, data = data, partial = True)
        if serialize.is_valid():
            serialize.save()
            return Response({'msg': 'Partial Data updated!'})
        return Response(serialize.errors)

    def delete(self, request, id=None, format=None):
        stu_obj = Student.objects.get(id=id)
        stu_obj.delete()
        return Response({'msg': 'Data deleted!'})



