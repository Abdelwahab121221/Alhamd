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
    al_syera = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Assistants(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Tables(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    date = models.DateField()
    num_pages = models.IntegerField()
    From = models.BigIntegerField()
    to = models.BigIntegerField()
    al_syera = models.TextField(max_length=40)
    is_here = models.BooleanField(default=False,null=False)
    def __str__(self):
        return f"{self.student}"
