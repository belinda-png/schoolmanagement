from django.db import models

# Create your models here.
class Teacher(models.Model):
    Name = models.CharField(max_length=20)
    Subject = models.CharField(max_length=30)
    Email = models.EmailField()
    number = models.IntegerField()
    class_name = models.CharField()
    def __str__(self):
        return self.Name
    
class Student(models.Model):
    name = models.CharField(max_length=20)
    age  = models.IntegerField()
    grade = models.CharField(max_length=5)
    cls = models.CharField(max_length=5)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,)
    def __str__(self):
        return self.name    

