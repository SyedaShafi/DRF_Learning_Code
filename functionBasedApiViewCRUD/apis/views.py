from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_apis(request, id=None):
    if request.method == 'GET':
        # id = request.data.get('id')
        # id = id
        if id is not None:
            stu_obj = Student.objects.get(id=id)
            serializer = StudentSerializer(stu_obj)
            return Response(serializer.data)
        
        stu_objs = Student.objects.all()
        serializer = StudentSerializer(stu_objs, many=True )
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = request.data
        serialize = StudentSerializer(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({'msg': 'Data Created'}, status = status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        data = request.data
        # id = request.data.get('id')
        student_obj = Student.objects.get(id=id)
        serialize = StudentSerializer(student_obj, data = data)

        if serialize.is_valid():
            serialize.save()
            return Response({'msg': 'Complete Data updated!'}, status=status.HTTP_200_OK)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        data = request.data
        # id = request.data.get('id')
        student_obj = Student.objects.get(id=id)
        serialize = StudentSerializer(student_obj, data = data, partial = True)

        if serialize.is_valid():
            serialize.save()
            return Response({'msg': 'Partial Data updated!'})
        Response(serialize.errors)


    if request.method == 'DELETE':
        # id = request.data.get('id')
        stu_obj = Student.objects.get(id=id)
        stu_obj.delete()
        return Response({'msg': 'Data deleted!'})



