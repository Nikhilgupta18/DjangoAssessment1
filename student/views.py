from django.shortcuts import render, get_object_or_404
from .models import Student, Section

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from django.http import HttpResponse

from student import serializers

import json


# Create your views here.

def index(request):
    students = Student.objects.all()
    context = {
        'hello': 'hello world',
        'students': students
    }
    return render(request,'index.html',context)


@api_view()
def getStudents(request):
    students = Student.objects.all()
    response = serializers.StudentSerializer(students, many=True)

    return Response(response.data)


@api_view(['POST'])
def createStudent(request):
    body = json.loads(request.body)
    response = serializers.StudentSerializer(data = body)

    if response.is_valid():
        inst = response.save()
        response = serializers.StudentSerializer(inst)
        return Response(response.data)
    
    return Response(response.errors)


@api_view()
def getSections(request):
    sections = Section.objects.all()
    response = serializers.SectionSerializer(sections, many=True)

    return Response(response.data)


@api_view(['POST'])
def createSection(request):
    body = json.loads(request.body)
    response = serializers.SectionSerializer(data = body)

    if response.is_valid():
        inst = response.save()
        response = serializers.SectionSerializer(inst)
        return Response(response.data)
    
    return Response(response.errors)


@api_view()
def getSectionWiseStudent(request, section):
    section = get_object_or_404(Section, name=section)
    students = Student.objects.filter(section=section)
    response = serializers.StudentSerializer(students, many=True)

    return Response(response.data)


@api_view(['POST'])
def updateSection(request, pk):
    section = Section.objects.get(pk=pk)
    body = json.loads(request.body)
    response = serializers.SectionSerializer(instance=section, data = body)

    if response.is_valid():
        inst = response.save()
        return Response(response.data)
    
    return Response(response.errors)


@api_view(['POST'])
def updateStudent(request, pk):
    body = json.loads(request.body)
    student = get_object_or_404(Student, pk=pk)
    serializer = serializers.StudentSerializer(student, data=body, partial=True)


    if serializer.is_valid():
        inst = serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)
