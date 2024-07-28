from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import status
from rest_framework.response import Response
from .serializers import AssistantsSerializer, TeacherSerializer, StudentSerializer , UserSerializer
from .models import Assistants ,Teacher ,Student
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def teachers(request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getTeacher(request , id):
    try:
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['GET','POST'])
def createTeacher(request):
    if request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(["GET","PUT"])
def updateTeacher(request ,id):
    try:
        teacher = Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
@api_view(['GET','DELETE'])
def deleteTeacher(request , id):
    try:
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(["GET"])
def students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStudent(request , id):
    try:
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST'])
def createStudent(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT"])
def updateStudent(request , id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

@api_view(['GET','DELETE'])
def deleteStudent(request , id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def assistants(request):
    assistants = Assistants.objects.all()
    serializer = AssistantsSerializer(assistants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAssistant(request , id):
    try:
        assistant = Assistants.objects.get(id=id)
        serializer = AssistantsSerializer(assistant)
        return Response(serializer.data)
    except Assistants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST'])
def createAssistant(request):
    if request.method == 'POST':
        serializer = AssistantsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT"])
def updateAssistant(request , id):
    try:
        assistant = Assistants.objects.get(id=id)
    except Assistants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = AssistantsSerializer(assistant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer = AssistantsSerializer(assistant)
        return Response(serializer.data)

@api_view(['GET','DELETE'])
def deleteAssistant(request , id):
    try:
        assistant = Assistants.objects.get(id=id)
        assistant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Assistants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
