from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView 
from . import views

urlpatterns = [
    path("Teachers", views.teachers, name="teachers"),
    path('Teachers/Teacher/<int:id>',views.getTeacher , name = 'get-Teacher'),
    path('Teachers/create',views.createTeacher,name='create-Teacher'),
    path('Teachers/update/<int:id>',views.updateTeacher , name='update-Teacher'),
    path('Teachers/delete/<int:id>',views.deleteTeacher ,name = 'delete-Teacher'),
    path("Students", views.students, name="students"),
    path('Students/Student/<int:id>',views.getStudent , name = 'get-Student'),
    path('Students/create',views.createStudent,name='create-Student'),
    path('Students/update/<int:id>',views.updateStudent , name='update-Student'),
    path('Students/delete/<int:id>',views.deleteStudent ,name = 'delete-Student'),
    path('Students/<str:teacher>',views.getStudentsByTeacherName , name = 'get-students-by-teacher-name'),
    path("Assistants", views.assistants, name="assistants"),
    path('Assistants/Assistant/<int:id>',views.getAssistant , name = 'get-Assistant'),
    path('Assistants/create',views.createAssistant,name='create-Assistant'),
    path('Assistants/update/<int:id>',views.updateAssistant , name='update-Assistant'),
    path('Assistants/delete/<int:id>',views.deleteAssistant ,name = 'delete-Assistant'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users',views.users , name = 'users'),
    path('users/create',views.createUser , name='create-user'),
    path('users/check user',views.checkUser,name='Check-user'),
    path('users/delete/<int:id>',views.deleteUser , name='delete-user'),
    path('users/update/<int:id>',views.updateUser , name='update-user'),
    path('users/user/<int:id>',views.getUser , name='create-user'),
]