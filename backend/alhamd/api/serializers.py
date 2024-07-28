from rest_framework import serializers
from .models import Student , Teacher , Assistants
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
class AssistantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistants
        fields = '__all__'