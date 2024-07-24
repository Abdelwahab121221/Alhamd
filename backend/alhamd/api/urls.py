from django.urls import path
from . import views

urlpatterns = [
    path("Teachers", views.teachers, name="teachers"),
    path('Teacher/<int:id>',views.getTeacher , name = 'get-Teacher'),
    path('Teachers/create',views.createTeacher,name='create-Teacher'),
    path('Teachers/update/<int:id>',views.updateTeacher , name='update-Teacher'),
    path('Teachers/delete/<int:id>',views.deleteTeacher ,name = 'delete-Teacher'),
    path("Students", views.students, name="students"),
    path('Student/<int:id>',views.getStudent , name = 'get-Student'),
    path('Students/create',views.createStudent,name='create-Student'),
    path('Students/update/<int:id>',views.updateStudent , name='update-Student'),
    path('Students/delete/<int:id>',views.deleteStudent ,name = 'delete-Student'),
    path("Assistants", views.assistants, name="students"),
    path('Assistant/<int:id>',views.getAssistant , name = 'get-Assistant'),
    path('Assistants/create',views.createAssistant,name='create-Assistant'),
    path('Assistants/update/<int:id>',views.updateAssistant , name='update-Assistant'),
    path('Assistants/delete/<int:id>',views.deleteAssistant ,name = 'delete-Assistant')
]