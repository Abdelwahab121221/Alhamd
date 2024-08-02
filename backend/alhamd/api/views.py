from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.views import status
from rest_framework.response import Response
from .serializers import AssistantsSerializer, TeacherSerializer, StudentSerializer , UserSerializer,TablesSerializer
from .models import Assistants ,Teacher ,Student , Tables
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
        @classmethod
        def get_token(cls, user):
            token = super().get_token(user)
            # Add custom claims
            token['username'] = user.username
            # ...
            return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
@permission_classes(IsAdminUser)
def users(request):
    return Response(UserSerializer(User.objects.all(),many=True).data)

@api_view(['POST'])
def checkUser(request):
    try:
        if User.objects.get(username = request.data['username']):
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response(status=status.HTTP_200_OK)
@api_view(['GET','POST'])
def createUser(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = UserSerializer(data = request.data)
        if user.is_valid():
            User.objects.create_user(username=username,password=password).save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(UserSerializer(User.objects.all(),many=True).data)
@api_view(['GET','DELETE'])
@permission_classes(IsAuthenticated)
def deleteUser(request,id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        serializer = UserSerializer(user)
        if serializer.is_valid:
            user.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(UserSerializer(User.objects.get(id=id)).data)
@api_view(['GET','PUT'])
@permission_classes(IsAuthenticated)
def updateUser(request,id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = UserSerializer(user,data = request.data)
        if serializer.is_valid:
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(UserSerializer(User.objects.get(id=id)).data)
@api_view(['GET'])
@permission_classes(IsAdminUser)
def getUser(request,id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(UserSerializer(User.objects.get(id=id)).data)
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
@permission_classes(IsAuthenticated)
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
@permission_classes(IsAuthenticated)
def deleteTeacher(request , id):
    try:
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(["GET"])
@permission_classes(IsAuthenticated)
def students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes(IsAuthenticated)
def getStudent(request , id):
    try:
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes(IsAuthenticated)
def getStudentsByTeacherName(request,teacher):
    first , last = teacher.split(' ')
    teacher_id = Teacher.objects.get(first_name = first , last_name = last).id
    students = Student.objects.filter(teacher= teacher_id)
    serializer = StudentSerializer(students,many=True).data
    return Response(serializer)
@api_view(['GET','POST'])
@permission_classes(IsAuthenticated)
def createStudent(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT"])
@permission_classes(IsAuthenticated)

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
@permission_classes(IsAuthenticated)

def deleteStudent(request , id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
@permission_classes(IsAuthenticated)

def assistants(request):
    assistants = Assistants.objects.all()
    serializer = AssistantsSerializer(assistants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes(IsAuthenticated)

def getAssistant(request , id):
    try:
        assistant = Assistants.objects.get(id=id)
        serializer = AssistantsSerializer(assistant)
        return Response(serializer.data)
    except Assistants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST'])
@permission_classes(IsAuthenticated)

def createAssistant(request):
    if request.method == 'POST':
        serializer = AssistantsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT"])
@permission_classes(IsAuthenticated)

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
@permission_classes(IsAuthenticated)

def deleteAssistant(request , id):
    try:
        assistant = Assistants.objects.get(id=id)
        assistant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Assistants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
