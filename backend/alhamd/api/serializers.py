from rest_framework import serializers
from .models import Student , Teacher , Assistants

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