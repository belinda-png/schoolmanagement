from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

def teacher_list(request):
        teachers = Teacher.objects.all()
        return render(request, 'teacher_list.html', {'teachers': teachers})
def addteacher(request):
       if request.method == "POST":
            form = AddTeacherForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Teacher Added Successfully!')
                return redirect('teacher_list')
            else:
                  form = AddTeacherForm()
                  messages.error(request, 'Please correct the error below.')
            return render(request, 'add_teacher.html', {'form': form})
def viewteacher(request, id):
      teacher_list = get_object_or_404(Teacher, pk=id)
      return render(request, 'view_teacher.html', {'teacher_list': teacher_list})

def updateteacher(request, id):
    teacher_list = get_object_or_404(Teacher, pk=id)
    if request.method =="POST":
        form = AddTeacherForm(request.POST, instance=teacher_list)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher Updated Successfully!')

            return redirect('teacher_list')     
        else:
            form = AddTeacherForm(instance=teacher_list)
            messages.error(request, 'Please correct the error below.')
            return render(request, 'update_teacher.html', {'form': form, 'teacher_list': teacher_list})

def deleteteacher(request, id):
        teacher_list = get_object_or_404(Teacher, pk=id)
        if request.method =="POST":
            teacher_list.delete()
            messages.success(request, 'Teacher Deleted Successfully!')
            return redirect('teacher_list')
        else:
             return render(request, 'delete_teacher.html', {'teacher_list': teacher_list})
def student_list(request):
        students = Student.objects.all()
        return render(request, 'student_list.html', {'students': students})

def addstudent(request):
     if request.method =="POST":
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Added Successfully!')
            return redirect('student_list')
        else:
             form = AddStudentForm()
             messages.error(request, 'Please correct the error below.')
             return render(request, 'add_student.html', {'form': form})

def viewstudent(request, id):
     student_list = get_object_or_404(Student, pk=id)
     return render(request, 'view_student.html', {'student_list': student_list})

def updatestudent(request,id):
     student_list = get_object_or_404(Student, pk=id)
     if request.method =="POST":
         form = AddStudentForm(request.POST, instance=student_list)
         if form.is_valid():
             form.save()
             messages.success(request, 'Student Updated Successfully!')
             return redirect('student_list')
         else:
              form = AddStudentForm(instance=student_list)
              messages.error(request, 'Please correct the error below.')
              return render(request, 'update_student.html', {'form': form, 'student_list': student_list})
def deletestudent(request, id):
     student_list = get_object_or_404(Student, pk=id)
     if request.method =="POST":
          student_list.delete()
          messages.success(request, 'Student Deleted Successfully!')
          return redirect('student_list')
     else:
          return render(request, 'delete_student.html', {'student_list': student_list})
                     
               