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