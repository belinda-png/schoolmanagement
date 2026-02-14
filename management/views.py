from django.shortcuts import render
from models import Teacher
from flask import request
# Create your views here.
def teacher_list(request):
        teachers = Teacher.objects.all()
        return render(request, 'teacher_list.html', {'teachers': teachers})
