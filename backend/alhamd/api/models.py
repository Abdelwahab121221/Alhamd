from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    is_finish = models.BooleanField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Assistants(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"